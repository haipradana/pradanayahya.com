<div class="dark:text-white">

# Smart Space (Jarvis) - Offline Voice Assistant

## Overview

Smart Space, atau Jarvis, adalah pipeline voice assistant lokal untuk otomasi ruang/lab di DTETI UGM. Sistem ini dirancang agar perintah suara bisa diproses secara lokal di perangkat edge, lalu diteruskan ke workflow otomasi untuk mengontrol perangkat seperti lampu, AC, dan proyektor.

Project ini menggabungkan ASR, TTS, LLM command understanding, dan otomasi N8N agar pengguna bisa berinteraksi dengan ruangan lewat bahasa natural.

## Pipeline

- **ASR**: Whisper untuk mengubah suara menjadi teks.
- **Command understanding**: LLM untuk memahami intent dan parameter perintah.
- **Automation**: N8N untuk menghubungkan hasil intent ke perangkat IoT.
- **TTS**: Piper voice untuk memberi respons suara.
- **Edge deployment**: Raspberry Pi sebagai target local-first deployment.

## Why It Matters

SmartLab/Jarvis dibuat untuk membuat ruang belajar atau laboratorium lebih mudah dikendalikan tanpa dashboard manual. Dengan pipeline lokal, sistem tetap bisa responsif dan lebih aman karena tidak semua interaksi perlu bergantung pada layanan cloud.

## Demo

- <a href="https://drive.google.com/file/u/1/d/15LTr5WR-MJreDqNmjXJ5QOjcOOM1l6Ez/view" target="_blank">Demo video</a>

</div>
