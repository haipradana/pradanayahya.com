"""
CLI entry point for syncing portfolio RAG data to Qdrant.

Run with:
    python -m app.sync_ingest
"""
import asyncio
import json

from .database import async_session_maker, init_db
from .ingest_service import sync_portfolio_files


async def main() -> None:
    await init_db()
    async with async_session_maker() as session:
        try:
            result = await sync_portfolio_files(session)
            await session.commit()
        except Exception:
            await session.rollback()
            raise
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    asyncio.run(main())
