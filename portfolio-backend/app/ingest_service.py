"""
Shared ingestion service for API and CLI-triggered Qdrant sync.
"""
import json
import hashlib
from pathlib import Path

from sqlalchemy.ext.asyncio import AsyncSession

from .embed import embed_text
from .models import IngestLog
from .qdrant_client import (
    delete_all_points,
    ensure_collection_exists,
    upsert_points_batch,
)


DATA_DIR = Path(__file__).parent.parent / "data" / "portfolio"


def get_data_dir() -> Path:
    """Ensure data directory exists and return path."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    return DATA_DIR


def make_point_id(item: dict, content: str) -> int:
    """Generate stable point ID from item id or content."""
    stable_id = item.get("id") or content
    return int(hashlib.md5(str(stable_id).encode()).hexdigest()[:8], 16)


async def sync_portfolio_files(db: AsyncSession) -> dict:
    """
    Sync all JSON files in the portfolio data directory to Qdrant.
    Clears existing data and re-ingests everything.
    """
    data_dir = get_data_dir()

    ensure_collection_exists()
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
                content = item.get("content", "")
                if not content:
                    continue

                dense, sparse = embed_text(content)
                points.append({
                    "id": make_point_id(item, content),
                    "dense": dense,
                    "sparse": sparse,
                    "payload": {
                        "category": item.get("category", item.get("type", "general")),
                        "title": item.get("title", ""),
                        "content": content,
                        "source_file": file_path.name,
                        **{
                            k: v
                            for k, v in item.items()
                            if k not in ["content", "category", "type", "title"]
                        },
                    },
                })

            if points:
                upsert_points_batch(points)

            log = IngestLog(
                filename=file_path.name,
                status="success",
                points_count=len(points),
            )
            db.add(log)
            logs.append({"filename": file_path.name, "status": "success", "points": len(points)})
            total_points += len(points)

        except Exception as e:
            log = IngestLog(
                filename=file_path.name,
                status="failed",
                points_count=0,
                error_message=str(e),
            )
            db.add(log)
            logs.append({"filename": file_path.name, "status": "failed", "error": str(e)})

    await db.flush()

    return {
        "success": True,
        "total_points": total_points,
        "files_processed": len(logs),
        "details": logs,
    }
