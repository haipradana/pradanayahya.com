<div class="dark:text-white">

# Sarcasm Detection with IndoBERT

## Overview

Project ini melakukan fine-tuning IndoBERT untuk klasifikasi sarkasme pada teks Bahasa Indonesia. Model mengklasifikasikan teks menjadi `sarcasm` atau `not sarcasm`.

Sarkasme sering sulit dikenali karena makna literal dan maksud sebenarnya bisa bertolak belakang. Karena itu, model berbasis transformer seperti IndoBERT dipakai untuk menangkap konteks kalimat secara lebih baik.

## Model

- Base model: IndoBERT
- Task: binary sequence classification
- Labels:
  - `0`: not sarcasm
  - `1`: sarcasm

## Evaluation

| Metric | Value |
|---|---:|
| Accuracy | 0.8378 |
| Precision | 0.8405 |
| Recall | 0.8286 |
| F1-Score | 0.8345 |

## Training Notes

Training dilakukan selama beberapa epoch dan dievaluasi pada test set. Model terbaik menjaga keseimbangan precision dan recall agar tidak terlalu mudah memberi label sarkasme pada kalimat biasa.

## Links

- <a href="https://huggingface.co/haipradana/indobert-indonesia-satire-sarcastic-classification-model" target="_blank">Hugging Face model</a>
- <a href="https://github.com/haipradana/indobert-indonesia-sarcastic-satire-classification" target="_blank">GitHub repository</a>

</div>
