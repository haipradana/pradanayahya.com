"""
Admin dashboard router - protected endpoints
"""
import uuid
from fastapi import APIRouter, Depends, HTTPException, Response, Request
from sqlalchemy import select, func, desc
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from ..database import get_db
from ..models import ContactSubmission, ChatSession, ChatMessage
from ..schemas import (
    LoginRequest, LoginResponse,
    ContactResponse, ContactListResponse,
    ChatSessionResponse, ChatSessionDetailResponse,
    DashboardStats
)
from ..auth import (
    authenticate, 
    get_current_admin, 
    delete_session,
    SESSION_COOKIE_NAME,
    require_admin
)

router = APIRouter(prefix="/api/admin", tags=["Admin"])


# ============ Auth ============

@router.post("/login", response_model=LoginResponse)
async def login(data: LoginRequest, response: Response):
    """Login to admin dashboard"""
    session_id = authenticate(data.username, data.password)
    
    if not session_id:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # Set session cookie
    response.set_cookie(
        key=SESSION_COOKIE_NAME,
        value=session_id,
        httponly=True,
        secure=True,  # HTTPS only
        samesite="lax",
        max_age=86400  # 24 hours
    )
    
    return LoginResponse(success=True, message="Login successful")


@router.post("/logout")
async def logout(request: Request, response: Response):
    """Logout from admin dashboard"""
    session_id = request.cookies.get(SESSION_COOKIE_NAME)
    
    if session_id:
        delete_session(session_id)
    
    response.delete_cookie(SESSION_COOKIE_NAME)
    return {"success": True, "message": "Logged out"}


@router.get("/me")
async def get_me(session: dict = require_admin):
    """Check if currently authenticated"""
    return {
        "authenticated": True,
        "username": session["username"]
    }


# ============ Contacts ============

@router.get("/contacts", response_model=list[ContactListResponse])
async def list_contacts(
    db: AsyncSession = Depends(get_db),
    _: dict = require_admin
):
    """List all contact submissions"""
    result = await db.execute(
        select(ContactSubmission)
        .order_by(desc(ContactSubmission.created_at))
    )
    contacts = result.scalars().all()
    
    return [
        ContactListResponse(
            id=c.id,
            name=c.name,
            email=c.email,
            message_preview=c.message[:100] + "..." if len(c.message) > 100 else c.message,
            is_read=c.is_read,
            created_at=c.created_at
        )
        for c in contacts
    ]


@router.get("/contacts/{contact_id}", response_model=ContactResponse)
async def get_contact(
    contact_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _: dict = require_admin
):
    """Get contact submission detail"""
    result = await db.execute(
        select(ContactSubmission).where(ContactSubmission.id == contact_id)
    )
    contact = result.scalar_one_or_none()
    
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    
    return contact


@router.patch("/contacts/{contact_id}/read")
async def mark_contact_read(
    contact_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _: dict = require_admin
):
    """Mark contact as read"""
    result = await db.execute(
        select(ContactSubmission).where(ContactSubmission.id == contact_id)
    )
    contact = result.scalar_one_or_none()
    
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    
    contact.is_read = True
    await db.flush()
    
    return {"success": True}


@router.delete("/contacts/{contact_id}")
async def delete_contact(
    contact_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _: dict = require_admin
):
    """Delete contact submission"""
    result = await db.execute(
        select(ContactSubmission).where(ContactSubmission.id == contact_id)
    )
    contact = result.scalar_one_or_none()
    
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    
    await db.delete(contact)
    await db.flush()
    
    return {"success": True}


# ============ Chats ============

@router.get("/chats", response_model=list[ChatSessionResponse])
async def list_chats(
    db: AsyncSession = Depends(get_db),
    _: dict = require_admin
):
    """List all chat sessions"""
    result = await db.execute(
        select(ChatSession)
        .options(selectinload(ChatSession.messages))
        .order_by(desc(ChatSession.updated_at))
    )
    sessions = result.scalars().all()
    
    return [
        ChatSessionResponse(
            id=s.id,
            created_at=s.created_at,
            updated_at=s.updated_at,
            message_count=s.message_count,
            preview=s.preview
        )
        for s in sessions
    ]


@router.get("/chats/{session_id}", response_model=ChatSessionDetailResponse)
async def get_chat(
    session_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _: dict = require_admin
):
    """Get chat session with all messages"""
    result = await db.execute(
        select(ChatSession)
        .options(selectinload(ChatSession.messages))
        .where(ChatSession.id == session_id)
    )
    session = result.scalar_one_or_none()
    
    if not session:
        raise HTTPException(status_code=404, detail="Chat session not found")
    
    return session


@router.delete("/chats/{session_id}")
async def delete_chat(
    session_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    _: dict = require_admin
):
    """Delete chat session and all messages"""
    result = await db.execute(
        select(ChatSession).where(ChatSession.id == session_id)
    )
    session = result.scalar_one_or_none()
    
    if not session:
        raise HTTPException(status_code=404, detail="Chat session not found")
    
    await db.delete(session)
    await db.flush()
    
    return {"success": True}


# ============ Stats ============

@router.get("/stats", response_model=DashboardStats)
async def get_stats(
    db: AsyncSession = Depends(get_db),
    _: dict = require_admin
):
    """Get dashboard statistics"""
    # Total contacts
    total_contacts = await db.scalar(
        select(func.count()).select_from(ContactSubmission)
    )
    
    # Unread contacts
    unread_contacts = await db.scalar(
        select(func.count())
        .select_from(ContactSubmission)
        .where(ContactSubmission.is_read == False)
    )
    
    # Total chats
    total_chats = await db.scalar(
        select(func.count()).select_from(ChatSession)
    )
    
    # Total messages
    total_messages = await db.scalar(
        select(func.count()).select_from(ChatMessage)
    )
    
    # Qdrant points - will be fetched from Qdrant client
    # For now, return 0 until we implement qdrant_client
    total_qdrant_points = 0
    
    return DashboardStats(
        total_contacts=total_contacts or 0,
        unread_contacts=unread_contacts or 0,
        total_chats=total_chats or 0,
        total_messages=total_messages or 0,
        total_qdrant_points=total_qdrant_points
    )
