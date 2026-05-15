"""
Contact form router - public endpoints
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import get_db
from ..models import ContactSubmission
from ..schemas import ContactCreate, ContactResponse

router = APIRouter(prefix="/api/contact", tags=["Contact"])


@router.post("", response_model=ContactResponse)
async def submit_contact(
    data: ContactCreate,
    db: AsyncSession = Depends(get_db)
):
    """
    Submit a contact form message.
    This is a public endpoint - no authentication required.
    """
    contact = ContactSubmission(
        name=data.name,
        email=data.email,
        message=data.message
    )
    
    db.add(contact)
    await db.flush()
    await db.refresh(contact)
    
    return contact
