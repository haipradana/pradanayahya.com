# pradanayahya.com

Personal portfolio website for Pradana Yahya Abdillah. The frontend is built with SvelteKit and Tailwind CSS, with a FastAPI backend for contact/admin features and a RAG-powered chat assistant.

## Features

- Portfolio pages for profile, projects, experience, and blog content.
- Floating chat widget connected to the portfolio backend.
- Backend contact/admin API with PostgreSQL persistence.
- RAG ingestion pipeline that embeds portfolio content into Qdrant.
- Automated backend sync from GitHub Actions to the VPS.
- Frontend deployment on Netlify.

## Tech Stack

- Frontend: SvelteKit, TypeScript, Tailwind CSS, Vite.
- Backend: FastAPI, PostgreSQL, Qdrant, FastEmbed, BytePlus LLM.
- Deployment: Netlify, Docker Compose, Traefik, GitHub Actions, Oracle VPS.

## Repository Structure

```text
.
├── src/                         # SvelteKit frontend
├── static/                      # Static assets and generated RAG payload
├── portfolio-backend/           # FastAPI backend and Docker config
├── .github/workflows/           # Backend deploy and RAG sync automation
├── package.json                 # Frontend scripts and dependencies
└── README.md
```

## Frontend Development

Install dependencies and start the local SvelteKit app:

```bash
npm install
npm run dev
```

Useful commands:

```bash
npm run check
npm run build
npm run preview
npm run rag:generate
```

The frontend API base URL is configured with:

```bash
VITE_API_URL=https://api.pradanayahya.com
```

## Backend Development

```bash
cd portfolio-backend
cp .env.example .env
docker compose up -d --build
```

Run RAG ingestion manually when needed:

```bash
docker compose exec -T portfolio-api python -m app.sync_ingest
```

The backend exposes health, admin, contact, chat, and ingestion endpoints. Secrets and runtime configuration live in `.env`, which is intentionally ignored by Git.

## Deployment

- Frontend changes are deployed by Netlify from the main branch.
- Backend changes are deployed by GitHub Actions to the VPS.
- Content updates can regenerate `static/rag/payload.json`, then the VPS backend syncs and embeds only changed payload records.
