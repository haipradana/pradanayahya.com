<div class="dark:text-white">

# KawanIsyarat - Komunikasi lewat BISINDO

## Overview

KawanIsyarat adalah aplikasi komunikasi dua arah antara pengguna Tuli BISINDO dan masyarakat dengar di Indonesia. Aplikasi ini berjalan offline setelah model awal diunduh, sehingga tidak membutuhkan server dan data pengguna tidak keluar dari perangkat.

Project ini meraih **Cactus Prize** pada **The Gemma 4 Good Challenge 2026** yang diselenggarakan Google DeepMind melalui Kaggle, dengan hadiah tim sebesar **US$10.000**. Tujuannya bukan menggantikan bahasa isyarat, tetapi membantu lebih banyak orang memahami dan merespons pengguna BISINDO dengan lebih baik.

## Penghargaan

Google mengumumkan KawanIsyarat sebagai pemenang Cactus Prize pada 24 Agustus 2026. Juri menyoroti **memory-aware model routing**, yang memuat Whisper saat dibutuhkan untuk transkripsi lalu melepasnya untuk memberi ruang bagi Gemma, serta optimasi latency agar aplikasi dapat digunakan secara interaktif pada smartphone Android.

Tim KawanIsyarat beranggotakan Pradana Yahya Abdillah, Maulana Isqi Habibah, dan Muhammad Ghozy Wira Elmada.

- <a href="https://blog.google/innovation-and-ai/technology/developers-tools/winning-entries-gemma-4-good-challenge/" target="_blank" rel="noopener noreferrer">Pengumuman resmi Google</a>
- <a href="https://jteti.ugm.ac.id/2026/09/18/mahasiswa-dteti-ugm-dan-tim-raih-cactus-prize-pada-the-gemma-4-good-challenge-2026/" target="_blank" rel="noopener noreferrer">Liputan DTETI UGM</a>

## Cara Kerja

**Tuli ke dengar**

Kamera, MediaPipe pose/hand landmarks, 1D CNN, gloss BISINDO, Gemma 4, kalimat Bahasa Indonesia natural, tips empati, lalu TTS.

**Dengar ke Tuli**

Mikrofon, WAV/PCM, Gemma 4 audio encoder, transcript, penyederhanaan oleh Gemma 4, lalu teks singkat yang lebih mudah dibaca.

## Fitur

- **Isyarat ke teks**: 1D CNN mengenali 16 kata BISINDO dari sequence 30 frame.
- **Suara ke teks sederhana**: Gemma 4 melakukan transkripsi audio dan menyederhanakan hasilnya.
- **Latihan alfabet**: latihan alfabet SIBI dan BISINDO dengan feedback visual.
- **Bantuan kosakata**: penjelasan kata sulit dalam Bahasa Indonesia sederhana.
- **Latihan artikulasi**: latihan pengucapan untuk pengguna dengar.
- **Emergency SOS**: TTS cepat untuk frasa penting seperti "Saya Tuli" dan "Saya butuh bantuan".
- **History**: log sesi dengan timestamp.

## Tech Stack

- **Framework**: Flutter, Riverpod, GoRouter
- **On-device AI**: Gemma 4 E2B INT4 via Cactus SDK
- **Gesture recognition**: MediaPipe + 1D Causal Depthwise CNN
- **STT**: Gemma 4 Audio Encoder, Whisper fallback
- **Local storage**: Hive
- **TTS**: flutter_tts

## Model Notes

- BISINDO gesture model memakai input 30 frames x 100 floats.
- 16 kelas kata: TULI, SAYA, KAMU, NAMA, TOLONG, APA, TERIMA_KASIH, BAIK, SAKIT, LAPAR, HAUS, MINTA, PAGI, MALAM, SEKOLAH, NOISE.
- Evaluasi LOSO mencapai 86.2% test accuracy.

## Links

- <a href="https://kawanisyarat.pradanayahya.com" target="_blank">Live demo</a>
- <a href="https://github.com/haipradana/KawanIsyarat" target="_blank">GitHub repository</a>
- <a href="https://youtu.be/eiXdkpwouBY" target="_blank">Demo video</a>

</div>
