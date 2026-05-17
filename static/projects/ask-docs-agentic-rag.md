<div class="dark:text-white">

# ask-docs - Agentic RAG Assistant

## Overview

ask-docs adalah implementasi Hybrid Search dan Agentic RAG dengan FastAPI backend dan React frontend. Sistem ini menggabungkan pencarian semantic berbasis dense vector embedding dengan pencarian exact keyword berbasis BM25, lalu menggabungkan hasilnya menggunakan Reciprocal Rank Fusion (RRF).

Pendekatan hybrid ini membuat jawaban lebih stabil: dense retrieval menangkap makna, BM25 menangkap kata kunci spesifik, dan RRF menyatukan ranking keduanya.

## Core Architecture

- **Hybrid Search**: dense vector search + BM25 sparse search.
- **Fusion**: Reciprocal Rank Fusion untuk ranking akhir.
- **Embedding model**: all-MiniLM-L6-v2 dengan 384 dimensi.
- **Vector database**: Qdrant.
- **Object storage**: MinIO.
- **LLM**: BytePlus.
- **Rooms**: knowledge base bisa dipisah per room seperti `kampus`, `umum`, `internal`, atau `dokumentasi`.

## Stack

### Backend

- FastAPI
- Qdrant
- MinIO
- all-MiniLM-L6-v2
- BytePlus LLM

### Frontend

- React 18
- TypeScript
- Vite
- Tailwind CSS
- Bun

## API Surface

- `POST /chat`: chat dengan AI menggunakan RAG.
- `POST /search`: search dokumen tanpa LLM.
- `POST /ingest`: ingest text manual.
- `POST /ingest/minio`: ingest PDF dari MinIO.

## Links

- <a href="https://ask.pradanayahya.com" target="_blank">Live demo</a>
- <a href="https://github.com/haipradana/ask-docs" target="_blank">GitHub repository</a>

</div>
