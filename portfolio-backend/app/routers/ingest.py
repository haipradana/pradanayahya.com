"""
Ingest router - JSON file management and Qdrant sync
"""
import json
import hashlib
from pathlib import Path
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import get_db
from ..models import IngestLog
from ..schemas import (
    IngestFileCreate, 
    IngestFileUpdate, 
    IngestFileResponse,
    IngestStatusResponse,
    IngestLogResponse
)
from ..auth import require_admin
from ..embed import embed_text
from ..qdrant_client import (
    upsert_points_batch, 
    delete_all_points,
    get_collection_info,
    ensure_collection_exists
)

router = APIRouter(prefix="/api/admin/ingest", tags=["Ingest"])

# Data directory path
DATA_DIR = Path(__file__).parent.parent.parent / "data" / "portfolio"


def get_data_dir() -> Path:
    """Ensure data directory exists and return path"""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    return DATA_DIR


def make_point_id(text: str) -> int:
    """Generate unique point ID from text hash"""
    return int(hashlib.md5(text.encode()).hexdigest()[:8], 16)


# ============ File Management ============

@router.get("/files", response_model=list[IngestFileResponse])
async def list_files(_: dict = require_admin):
    """List all JSON files in the data directory"""
    data_dir = get_data_dir()
    files = []
    
    for file_path in data_dir.glob("*.json"):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = json.load(f)
                files.append(IngestFileResponse(
                    filename=file_path.name,
                    item_count=len(content) if isinstance(content, list) else 1
                ))
        except (json.JSONDecodeError, IOError):
            files.append(IngestFileResponse(
                filename=file_path.name,
                item_count=0
            ))
    
    return files


@router.get("/files/{filename}")
async def get_file(filename: str, _: dict = require_admin):
    """Get content of a specific JSON file"""
    data_dir = get_data_dir()
    file_path = data_dir / filename
    
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found")
    
    if not file_path.suffix == ".json":
        raise HTTPException(status_code=400, detail="Only JSON files allowed")
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = json.load(f)
        return {"filename": filename, "content": content}
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON file")


@router.post("/files")
async def create_file(data: IngestFileCreate, _: dict = require_admin):
    """Create a new JSON file"""
    data_dir = get_data_dir()
    
    # Ensure .json extension
    filename = data.filename if data.filename.endswith(".json") else f"{data.filename}.json"
    file_path = data_dir / filename
    
    if file_path.exists():
        raise HTTPException(status_code=400, detail="File already exists")
    
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data.content, f, ensure_ascii=False, indent=2)
        return {"success": True, "filename": filename}
    except IOError as e:
        raise HTTPException(status_code=500, detail=f"Failed to create file: {e}")


@router.put("/files/{filename}")
async def update_file(filename: str, data: IngestFileUpdate, _: dict = require_admin):
    """Update an existing JSON file"""
    data_dir = get_data_dir()
    file_path = data_dir / filename
    
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found")
    
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data.content, f, ensure_ascii=False, indent=2)
        return {"success": True, "filename": filename}
    except IOError as e:
        raise HTTPException(status_code=500, detail=f"Failed to update file: {e}")


@router.delete("/files/{filename}")
async def delete_file(filename: str, _: dict = require_admin):
    """Delete a JSON file"""
    data_dir = get_data_dir()
    file_path = data_dir / filename
    
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found")
    
    try:
        file_path.unlink()
        return {"success": True}
    except IOError as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete file: {e}")


# ============ Sync to Qdrant ============

@router.post("/sync")
async def sync_to_qdrant(
    db: AsyncSession = Depends(get_db),
    _: dict = require_admin
):
    """
    Sync all JSON files to Qdrant.
    Clears existing data and re-ingests everything.
    """
    data_dir = get_data_dir()
    
    # Ensure collection exists
    ensure_collection_exists()
    
    # Clear existing points
    delete_all_points()
    
    total_points = 0
    logs = []
    
    for file_path in data_dir.glob("*.json"):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                items = json.load(f)
            
            if not isinstance(items, list):
                items = [items]
            
            points = []
            for item in items:
                # Get the text content to embed
                content = item.get("content", "")
                if not content:
                    continue
                
                # Generate embeddings
                dense, sparse = embed_text(content)
                
                # Create point
                point_id = make_point_id(content)
                points.append({
                    "id": point_id,
                    "dense": dense,
                    "sparse": sparse,
                    "payload": {
                        "category": item.get("category", item.get("type", "general")),
                        "title": item.get("title", ""),
                        "content": content,
                        "source_file": file_path.name,
                        **{k: v for k, v in item.items() if k not in ["content", "category", "type", "title"]}
                    }
                })
            
            # Batch upsert
            if points:
                upsert_points_batch(points)
            
            # Log success
            log = IngestLog(
                filename=file_path.name,
                status="success",
                points_count=len(points)
            )
            db.add(log)
            logs.append({"filename": file_path.name, "status": "success", "points": len(points)})
            total_points += len(points)
            
        except Exception as e:
            # Log failure
            log = IngestLog(
                filename=file_path.name,
                status="failed",
                points_count=0,
                error_message=str(e)
            )
            db.add(log)
            logs.append({"filename": file_path.name, "status": "failed", "error": str(e)})
    
    await db.flush()
    
    return {
        "success": True,
        "total_points": total_points,
        "files_processed": len(logs),
        "details": logs
    }


@router.get("/status")
async def get_status(
    db: AsyncSession = Depends(get_db),
    _: dict = require_admin
):
    """Get current sync status"""
    # Get latest log
    result = await db.execute(
        select(IngestLog)
        .order_by(desc(IngestLog.created_at))
        .limit(1)
    )
    latest_log = result.scalar_one_or_none()
    
    # Get collection info from Qdrant
    collection_info = get_collection_info()
    
    # Get file list
    data_dir = get_data_dir()
    files = []
    for file_path in data_dir.glob("*.json"):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = json.load(f)
                files.append(IngestFileResponse(
                    filename=file_path.name,
                    item_count=len(content) if isinstance(content, list) else 1
                ))
        except:
            pass
    
    return {
        "last_sync": latest_log.created_at if latest_log else None,
        "total_points": collection_info.get("points_count", 0),
        "collection_status": collection_info.get("status", "unknown"),
        "files": files
    }


@router.get("/logs", response_model=list[IngestLogResponse])
async def get_logs(
    limit: int = 10,
    db: AsyncSession = Depends(get_db),
    _: dict = require_admin
):
    """Get recent ingest logs"""
    result = await db.execute(
        select(IngestLog)
        .order_by(desc(IngestLog.created_at))
        .limit(limit)
    )
    return result.scalars().all()
