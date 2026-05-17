<div class="dark:text-white">

# DATATHON 2025 - Retail Behaviour Analysis

## Overview

Sistem analitik berbasis AI untuk optimalisasi strategi bisnis melalui analisis perilaku pelanggan dari rekaman CCTV. Menggunakan computer vision dan multimodal transformer untuk memberikan insights actionable bagi strategi bisnis retail.

<center>
<a href="https://youtu.be/ZtWqnMJQmu0" target="_blank">
<img src="/images/projects/datathon_2025-1/retail-behaviour-1.webp" width="55%">
</a>
</center>

## Key Features

- **Segmentasi Rak**: YOLOv11-seg (94.73% precision, 73.37% recall)
- **Pelacakan Multi-Person**: ByteTrack untuk tracking video
- **Klasifikasi Aksi**: TimeSFormer dengan domain adaptation (75.0% accuracy)
- **Analisis Behavior**: Heat-map, dwell-time, dan traffic analysis
- **6 Action Classes**: Reach/Retract from Shelf, Hand in Shelf, Inspect Product/Shelf, Background

## Outputs

- Heat-map visualisasi traffic pelanggan
- Statistik interaksi per rak
- Statistik dwell time setiap pelanggan
- Rekomendasi optimasi layout toko dari keramaian rak
- Comprehensive behavioral insights

## Datasets HuggingFace

- <a href="https://huggingface.co/datasets/haipradana/merl-shopping-action-detection" target="_blank">MERL Dataset</a>
- <a href="https://huggingface.co/datasets/haipradana/action" target="_blank">CCTV-Like Dataset</a>
- <a href="https://huggingface.co/datasets/cheesecz/shelf-segmentation-train" target="_blank">Shelf Segmentation</a>

## Models HuggingFace

- <a href="https://huggingface.co/haipradana/s-h-o-p-domain-adaptation" target="_blank">Action Recognition Model - Domain Adaptation</a>
- <a href="https://huggingface.co/cheesecz/shelf-segmentation" target="_blank">Shelf Segmentation</a>
- <a href="https://huggingface.co/cheesecz/object-tracking" target="_blank">YOLOv11 Model</a>

## Deployment

Pipeline ini sudah dideploy di <a href="https://huggingface.co/spaces/haipradana/retail-behavior-analysis" target="_blank">Hugging Face Space</a>

### Demo Video dan Dokumentasi

<center>
<a href="https://youtu.be/ZtWqnMJQmu0" target="_blank" style="color:#2563eb; text-decoration:underline;">Lihat Demo Video</a>

<a href="https://youtu.be/ZtWqnMJQmu0" target="_blank">
<img src="/images/projects/datathon_2025-1/retail-behaviour-1.webp" width="100%">
</a>
</center>

</div>
