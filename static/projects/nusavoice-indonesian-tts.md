<div class="dark:text-white">

# NusaVoice - Lightweight Indonesian Text-to-Speech

## Overview

NusaVoice adalah model Text-to-Speech Bahasa Indonesia yang ringan dan bisa berjalan di CPU-only hardware. Project ini berfokus pada fine-tuning Piper TTS untuk menghasilkan suara Bahasa Indonesia yang natural, cepat, dan mudah di-deploy.

Berbeda dari pendekatan LLM on-device, NusaVoice adalah sistem TTS berbasis Piper/VITS. Modelnya dilatih untuk pola pengucapan Bahasa Indonesia, lalu disajikan melalui backend FastAPI dan frontend web.

## Model Details

| Voice | Training Data | Architecture |
|---|---|---|
| Male | Audiobook dan podcast recordings | Piper VITS |
| Female | Audiobook recordings | Piper VITS |

Kedua model dibuat dari arsitektur Piper dan dioptimalkan untuk inference real-time yang ringan.

## Tech Stack

- **TTS engine**: Piper
- **Architecture**: VITS
- **Backend**: FastAPI
- **Frontend**: React, Vite, Tailwind CSS
- **Runtime target**: CPU-only inference

## Project Structure

```text
NusaVoice/
├── nusavoice-frontend/    # React + Vite + Tailwind
└── nusavoice-backend/     # FastAPI + Piper TTS
```

## Links

- <a href="https://nusavoice.pradanayahya.com" target="_blank">Live demo</a>
- <a href="https://github.com/haipradana/NusaVoice" target="_blank">GitHub repository</a>

</div>
