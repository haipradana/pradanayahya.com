"""
Pydantic schemas for request/response validation
"""
import uuid
from datetime import datetime
from pydantic import BaseModel, EmailStr


# ============ Contact ============

class ContactCreate(BaseModel):
    name: str
    email: EmailStr
    message: str


class ContactResponse(BaseModel):
    id: uuid.UUID
    name: str
    email: str
    message: str
    is_read: bool
    created_at: datetime
    
    class Config:
        from_attributes = True


class ContactListResponse(BaseModel):
    id: uuid.UUID
    name: str
    email: str
    message_preview: str
    is_read: bool
    created_at: datetime


# ============ Chat ============

class ChatCreate(BaseModel):
    session_id: uuid.UUID | None = None
    message: str


class ChatResponse(BaseModel):
    session_id: uuid.UUID
    answer: str
    sources: list[dict] = []


class ChatMessageResponse(BaseModel):
    id: uuid.UUID
    role: str
    content: str
    created_at: datetime
    
    class Config:
        from_attributes = True


class ChatSessionResponse(BaseModel):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    message_count: int
    preview: str
    
    class Config:
        from_attributes = True


class ChatSessionDetailResponse(BaseModel):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    messages: list[ChatMessageResponse]
    
    class Config:
        from_attributes = True


# ============ Auth ============

class LoginRequest(BaseModel):
    username: str
    password: str


class LoginResponse(BaseModel):
    success: bool
    message: str


# ============ Ingest ============

class IngestFileCreate(BaseModel):
    filename: str
    content: list[dict]


class IngestFileUpdate(BaseModel):
    content: list[dict]


class IngestFileResponse(BaseModel):
    filename: str
    item_count: int


class IngestStatusResponse(BaseModel):
    last_sync: datetime | None
    total_points: int
    files: list[IngestFileResponse]


class IngestLogResponse(BaseModel):
    id: uuid.UUID
    filename: str
    status: str
    points_count: int
    error_message: str | None
    created_at: datetime
    
    class Config:
        from_attributes = True


# ============ Stats ============

class DashboardStats(BaseModel):
    total_contacts: int
    unread_contacts: int
    total_chats: int
    total_messages: int
    total_qdrant_points: int
