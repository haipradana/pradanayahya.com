<div class="dark:text-white">

# IndoBERT NER for Indonesian Culinary Text

## Overview

Project ini adalah pipeline Named Entity Recognition untuk teks kuliner Bahasa Indonesia. Sistem dibuat untuk ACTION UNESA 2025 Data Mining Competition dan meraih 3rd Place dengan Micro-F1 0.8411 pada leaderboard Kaggle.

Tujuannya adalah mengenali entitas penting dari teks kuliner, seperti nama makanan, bahan, lokasi, atau atribut lain yang relevan dengan domain kuliner Indonesia.

## Approach

- Fine-tuning IndoBERT untuk token classification.
- Preprocessing teks Bahasa Indonesia agar format token dan label konsisten.
- Evaluasi menggunakan Micro-F1, metrik yang umum dipakai untuk sequence labeling.
- Iterasi eksperimen pada cleaning, token alignment, dan training configuration.

## Why IndoBERT

IndoBERT dipilih karena sudah dilatih pada korpus Bahasa Indonesia, sehingga lebih cocok untuk menangkap konteks lokal, variasi kata, dan struktur kalimat Indonesia dibanding model multilingual umum.

## Result

- **Competition**: ACTION UNESA 2025 Data Mining Competition
- **Placement**: 3rd Place
- **Task**: Indonesian culinary Named Entity Recognition
- **Model**: IndoBERT token classification
- **Leaderboard score**: Micro-F1 0.8411

</div>
