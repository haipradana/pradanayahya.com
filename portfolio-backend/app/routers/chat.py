"""
Chat router - AI chatbot with RAG
"""
import uuid
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from ..database import get_db
from ..models import ChatSession, ChatMessage
from ..schemas import ChatCreate, ChatResponse
from ..embed import embed_text
from ..qdrant_client import hybrid_search, list_payloads_by_category
from ..llm import generate_answer

router = APIRouter(prefix="/api/chat", tags=["Chat"])


def requested_listing(message: str) -> str | None:
    """Detect broad listing requests that need full category context."""
    text = message.lower()
    listing_words = (
        "apa saja",
        "list",
        "daftar",
        "semua",
        "sebutkan",
        "tampilkan",
    )
    if not any(word in text for word in listing_words):
        return None

    if any(word in text for word in ("project", "projek", "portfolio", "portofolio")):
        return "project"
    if any(word in text for word in ("experience", "pengalaman")):
        return "experience"
    if any(word in text for word in ("award", "penghargaan", "juara", "prestasi")):
        return "award"
    if any(word in text for word in ("education", "pendidikan", "kuliah")):
        return "education"
    return None


def build_listing_context(category: str) -> tuple[str, list[dict]]:
    """Build context from every payload in a Qdrant category."""
    payloads = list_payloads_by_category(category)
    payloads.sort(key=lambda item: (item.get("year") or 0, item.get("title") or ""), reverse=True)

    context_parts = []
    sources = []
    for payload in payloads:
        text = payload.get("content", payload.get("text", ""))
        if not text:
            continue
        context_parts.append(text)
        sources.append({
            "category": payload.get("category", "unknown"),
            "title": payload.get("title", ""),
            "score": 1.0,
        })

    return "\n\n".join(context_parts), sources


@router.post("/session")
async def create_session(db: AsyncSession = Depends(get_db)):
    """Create a new chat session"""
    session = ChatSession()
    db.add(session)
    await db.flush()
    await db.refresh(session)
    
    return {"session_id": str(session.id)}


@router.post("", response_model=ChatResponse)
async def chat(
    data: ChatCreate,
    db: AsyncSession = Depends(get_db)
):
    """
    Send a message and get AI response.
    Creates session automatically if not provided.
    """
    # Get or create session
    if data.session_id:
        result = await db.execute(
            select(ChatSession).where(ChatSession.id == data.session_id)
        )
        session = result.scalar_one_or_none()
        
        if not session:
            raise HTTPException(status_code=404, detail="Session not found")
    else:
        session = ChatSession()
        db.add(session)
        await db.flush()
        await db.refresh(session)
    
    # Save user message
    user_message = ChatMessage(
        session_id=session.id,
        role="user",
        content=data.message
    )
    db.add(user_message)
    
    listing_category = requested_listing(data.message)
    if listing_category:
        context, sources = build_listing_context(listing_category)
    else:
        # Embed the question
        dense, sparse = embed_text(data.message)
        
        # Hybrid search for relevant context
        results = hybrid_search(
            dense=dense,
            sparse=sparse,
            limit=5
        )
        
        # Build context from search results
        context_parts = []
        sources = []
        
        for r in results:
            if r.payload:
                text = r.payload.get("content", r.payload.get("text", ""))
                if text:
                    context_parts.append(text)
                    sources.append({
                        "category": r.payload.get("category", "unknown"),
                        "title": r.payload.get("title", ""),
                        "score": r.score
                    })
        
        context = "\n\n".join(context_parts)
    
    # Generate answer
    if context:
        answer = generate_answer(data.message, context)
    else:
        answer = (
            "Halo! 👋 Saya Latent, asisten AI di portfolio Pradana. "
            "Sepertinya saya belum punya informasi spesifik tentang itu. "
            "Coba tanya tentang project, skills, atau pengalaman Pradana! 😊"
        )
    
    # Save assistant message
    assistant_message = ChatMessage(
        session_id=session.id,
        role="assistant",
        content=answer
    )
    db.add(assistant_message)
    
    # Update session timestamp
    session.updated_at = datetime.utcnow()
    
    await db.flush()
    
    return ChatResponse(
        session_id=session.id,
        answer=answer,
        sources=sources[:10]
    )


@router.get("/session/{session_id}/messages")
async def get_session_messages(
    session_id: uuid.UUID,
    db: AsyncSession = Depends(get_db)
):
    """Get all messages for a session (for chat history restoration)"""
    result = await db.execute(
        select(ChatSession)
        .options(selectinload(ChatSession.messages))
        .where(ChatSession.id == session_id)
    )
    session = result.scalar_one_or_none()
    
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    
    return {
        "session_id": str(session.id),
        "messages": [
            {
                "role": msg.role,
                "content": msg.content,
                "created_at": msg.created_at.isoformat()
            }
            for msg in session.messages
        ]
    }
