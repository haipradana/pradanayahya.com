"""
Embedding functions for dense and sparse vectors
Using fastembed for efficient CPU-based embedding
"""
from fastembed import TextEmbedding, SparseTextEmbedding


# Dense embedding model (MiniLM - fast and good quality)
dense_model = TextEmbedding(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Sparse embedding model (BM25 for keyword matching)
sparse_model = SparseTextEmbedding(
    model_name="Qdrant/bm25"
)


def embed_dense(text: str) -> list[float]:
    """
    Generate dense embedding for text.
    Returns a 384-dimensional vector.
    """
    return list(dense_model.embed([text]))[0].tolist()


def embed_sparse(text: str) -> dict:
    """
    Generate sparse embedding for text using BM25.
    Returns dict with 'indices' and 'values' for sparse vector.
    """
    emb = list(sparse_model.embed([text]))[0]
    return {
        "indices": emb.indices.tolist(),
        "values": emb.values.tolist()
    }


def embed_text(text: str) -> tuple[list[float], dict]:
    """
    Generate both dense and sparse embeddings.
    Returns (dense_vector, sparse_vector_dict)
    """
    dense = embed_dense(text)
    sparse = embed_sparse(text)
    return dense, sparse
