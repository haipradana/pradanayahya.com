"""
Simple session-based authentication for admin dashboard
"""
import hashlib
import secrets
from datetime import datetime, timedelta
from functools import wraps

from fastapi import Request, HTTPException, Depends
from fastapi.responses import JSONResponse

from .config import settings


# In-memory session store (simple approach for single-instance deployment)
# For production with multiple instances, use Redis
sessions: dict[str, dict] = {}

SESSION_COOKIE_NAME = "admin_session"
SESSION_EXPIRY_HOURS = 24


def hash_password(password: str) -> str:
    """Simple password hash using SHA256"""
    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(password: str, hashed: str) -> bool:
    """Verify password against hash"""
    return hash_password(password) == hashed


def create_session(username: str) -> str:
    """Create a new session and return session ID"""
    session_id = secrets.token_urlsafe(32)
    sessions[session_id] = {
        "username": username,
        "created_at": datetime.utcnow(),
        "expires_at": datetime.utcnow() + timedelta(hours=SESSION_EXPIRY_HOURS)
    }
    return session_id


def get_session(session_id: str) -> dict | None:
    """Get session data if valid"""
    session = sessions.get(session_id)
    if not session:
        return None
    
    if datetime.utcnow() > session["expires_at"]:
        # Session expired, remove it
        del sessions[session_id]
        return None
    
    return session


def delete_session(session_id: str) -> bool:
    """Delete a session"""
    if session_id in sessions:
        del sessions[session_id]
        return True
    return False


def authenticate(username: str, password: str) -> str | None:
    """
    Authenticate admin user.
    Returns session_id if successful, None otherwise.
    """
    if username == settings.admin_username and password == settings.admin_password:
        return create_session(username)
    return None


async def get_current_admin(request: Request) -> dict:
    """
    Dependency to verify admin session.
    Returns session data if authenticated.
    """
    session_id = request.cookies.get(SESSION_COOKIE_NAME)
    
    if not session_id:
        raise HTTPException(
            status_code=401,
            detail="Not authenticated"
        )
    
    session = get_session(session_id)
    if not session:
        raise HTTPException(
            status_code=401,
            detail="Session expired or invalid"
        )
    
    return session


# Dependency for protected routes
require_admin = Depends(get_current_admin)
