"""
Qdrant client for hybrid search with Reciprocal Rank Fusion
"""
from qdrant_client import QdrantClient
from qdrant_client.models import (
    PointStruct, 
    SparseVector,
    Prefetch,
    FusionQuery,
    Filter,
    FieldCondition,
    MatchValue,
    VectorParams,
    SparseVectorParams,
    Distance
)

from .config import settings


# Initialize Qdrant client
client = QdrantClient(
    host=settings.qdrant_url,
    port=443,
    https=True,
    api_key=settings.qdrant_api_key,
    timeout=120.0,
    prefer_grpc=False
)


def ensure_collection_exists():
    """Create collection if it doesn't exist"""
    collections = client.get_collections().collections
    collection_names = [c.name for c in collections]
    
    if settings.collection_name not in collection_names:
        client.create_collection(
            collection_name=settings.collection_name,
            vectors_config={
                "dense": VectorParams(
                    size=384,  # MiniLM embedding size
                    distance=Distance.COSINE
                )
            },
            sparse_vectors_config={
                "sparse": SparseVectorParams()
            }
        )
        print(f"✅ Created collection: {settings.collection_name}")
    
    return True


def get_collection_info() -> dict:
    """Get collection info including point count"""
    try:
        info = client.get_collection(settings.collection_name)
        return {
            "name": settings.collection_name,
            "points_count": info.points_count,
            "status": info.status.value
        }
    except Exception as e:
        return {
            "name": settings.collection_name,
            "points_count": 0,
            "status": "not_found",
            "error": str(e)
        }


def upsert_point(
    point_id: int,
    dense: list[float],
    sparse: dict,
    payload: dict
):
    """Upsert a single point to the collection"""
    client.upsert(
        collection_name=settings.collection_name,
        points=[
            PointStruct(
                id=point_id,
                vector={
                    "dense": dense,
                    "sparse": SparseVector(
                        indices=sparse["indices"],
                        values=sparse["values"]
                    )
                },
                payload=payload
            )
        ]
    )


def upsert_points_batch(points: list[dict]):
    """
    Upsert multiple points in batch.
    Each point dict should have: id, dense, sparse, payload
    """
    point_structs = [
        PointStruct(
            id=p["id"],
            vector={
                "dense": p["dense"],
                "sparse": SparseVector(
                    indices=p["sparse"]["indices"],
                    values=p["sparse"]["values"]
                )
            },
            payload=p["payload"]
        )
        for p in points
    ]
    
    client.upsert(
        collection_name=settings.collection_name,
        points=point_structs
    )


def delete_all_points():
    """Delete all points in the collection (for re-sync)"""
    try:
        # Recreate collection to clear all points
        client.delete_collection(settings.collection_name)
        ensure_collection_exists()
        return True
    except Exception as e:
        print(f"Error deleting points: {e}")
        return False


def hybrid_search(
    dense: list[float],
    sparse: dict,
    limit: int = 5,
    category_filter: str | None = None
) -> list:
    """
    Perform hybrid search using Reciprocal Rank Fusion (RRF).
    Combines dense (semantic) and sparse (keyword) search.
    """
    # Build filter if category specified
    query_filter = None
    if category_filter:
        query_filter = Filter(
            must=[
                FieldCondition(
                    key="category",
                    match=MatchValue(value=category_filter)
                )
            ]
        )
    
    # Hybrid search with RRF
    response = client.query_points(
        collection_name=settings.collection_name,
        prefetch=[
            Prefetch(
                query=dense,
                using="dense",
                limit=limit * 2,
                filter=query_filter
            ),
            Prefetch(
                query=SparseVector(
                    indices=sparse["indices"],
                    values=sparse["values"]
                ),
                using="sparse",
                limit=limit * 2,
                filter=query_filter
            )
        ],
        query=FusionQuery(fusion="rrf"),
        limit=limit,
        with_payload=True
    )
    
    return response.points
