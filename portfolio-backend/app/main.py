"""
Portfolio Backend - Main FastAPI Application
"""
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import settings
from .database import init_db
from .qdrant_client import get_collection_info
from .routers import contact, admin, chat, ingest


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan events"""
    # Startup
    await init_db()
    print("✅ Database initialized")
    yield
    # Shutdown
    print("👋 Shutting down...")


app = FastAPI(
    title="Portfolio Backend API",
    description="Backend for pradanayahya.com - Contact form, AI chatbot, and admin dashboard",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(contact.router)
app.include_router(admin.router)
app.include_router(chat.router)
app.include_router(ingest.router)


@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "Portfolio Backend API",
        "version": "1.0.0"
    }


@app.get("/health")
async def health():
    """Detailed health check"""
    qdrant_info = get_collection_info()
    return {
        "status": "healthy",
        "database": "connected",
        "qdrant": qdrant_info.get("status", "unknown"),
        "qdrant_points": qdrant_info.get("points_count", 0)
    }
