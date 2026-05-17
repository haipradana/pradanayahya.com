<div class="dark:text-white">

# Hate Speech Classification with RoBERTa

## Overview

Project ini melakukan fine-tuning RoBERTa untuk klasifikasi hate speech pada tweet Bahasa Indonesia. Model mengklasifikasikan teks menjadi dua label: neutral dan hate.

Dataset dibuat dari gabungan data scraping Twitter dan beberapa dataset publik dari GitHub, lalu dibersihkan dan dipreprocess sebelum training.

## Dataset

Dataset yang sudah dibersihkan tersedia di Hugging Face:

- <a href="https://huggingface.co/haipradana/indonesian-twitter-hate-speech-cleaned" target="_blank">haipradana/indonesian-twitter-hate-speech-cleaned</a>

## Model

- Base model: `cardiffnlp/twitter-roberta-base-sentiment-latest`
- Task: binary sequence classification
- Labels:
  - `0`: neutral
  - `1`: hate

## Performance

| Metric | Value |
|---|---:|
| Accuracy | 82.01% |
| Precision | 82.68% |
| Recall | 81.72% |
| F1-Score | 82.19% |

## Usage

Model bisa digunakan dengan `transformers` untuk inference teks tunggal, atau lewat script `scripts/predict.py` yang tersedia di repository.

## Links

- <a href="https://huggingface.co/haipradana/roberta-hate-classification-model" target="_blank">Hugging Face model</a>
- <a href="https://github.com/haipradana/RoBERTa-Indonesian-Hate-Tweet-Classification" target="_blank">GitHub repository</a>

</div>
