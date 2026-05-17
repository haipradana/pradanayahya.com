<div class="dark:text-white">

# BMKG-Hirup - PM2.5 Air Quality Forecasting

## Overview

Hirup adalah aplikasi web untuk memprediksi kualitas udara PM2.5. Project ini dikembangkan saat magang di Stasiun Klimatologi Yogyakarta sebagai sistem machine learning yang mengubah data cuaca dan histori PM2.5 menjadi prediksi yang bisa dipakai lewat aplikasi web.

PM2.5 adalah partikel polusi udara berukuran lebih kecil dari 2.5 mikrometer. Karena ukurannya sangat kecil, PM2.5 bisa masuk jauh ke paru-paru dan berdampak pada kesehatan. Hirup dibuat untuk membantu kalkulasi, estimasi, dan prediksi PM2.5 secara lebih cepat.

## What I Built

- Model prediksi PM2.5 berbasis Random Forest Regressor.
- Backend FastAPI untuk melayani prediksi model.
- Frontend React + Vite untuk input data dan visualisasi hasil.
- Pipeline preprocessing dan training di Python.
- Deployment berbasis Docker di VPS.

## Tech Stack

- **Frontend**: React, Vite, TypeScript
- **Backend**: FastAPI, Python
- **Machine Learning**: Random Forest Regressor, scikit-learn
- **Deployment**: Docker, VPS

## Links

- <a href="https://bmkg-hirup.pradanayahya.com" target="_blank">Live demo</a>
- <a href="https://github.com/haipradana/hirup" target="_blank">GitHub repository</a>

## Data Note

Dataset mentah dari alat AWS dan dokumen EDA tidak dipublikasikan karena bersifat internal dan confidential milik BMKG. Repositori publik berisi kode implementasi sistem, arsitektur model, dan struktur aplikasi.

</div>
