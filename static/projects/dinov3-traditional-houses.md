<div class="dark:text-white">

# DINOv3 + Pseudo-labeling for Indonesian Traditional Houses

## Overview

Project ini adalah pipeline klasifikasi gambar rumah adat Indonesia untuk DSC LOGIKA UI 2025. Sistem menggunakan DINOv3 sebagai feature extractor dan pseudo-labeling untuk memanfaatkan data tidak berlabel secara semi-supervised.

Hasil akhirnya meraih 2nd Place dengan test accuracy 97.21%.

## Approach

- Menggunakan DINOv3 untuk mengekstrak representasi visual dari gambar rumah adat.
- Melatih classifier di atas embedding visual.
- Memakai pseudo-labeling untuk memperluas sinyal training dari data unlabeled.
- Melakukan iterasi thresholding agar pseudo-label yang dipakai tetap cukup confident.
- Mengevaluasi pipeline pada data test kompetisi.

## Why DINOv3

DINOv3 cocok untuk skenario data terbatas karena representasi visualnya kuat tanpa harus melatih CNN dari awal. Untuk dataset rumah adat yang memiliki variasi sudut, material, dan bentuk arsitektur, feature extractor yang sudah kuat membantu model fokus pada pola visual penting.

## Result

- **Competition**: DSC LOGIKA UI 2025
- **Placement**: 2nd Place
- **Task**: Indonesian traditional house image classification
- **Method**: DINOv3 features + pseudo-labeling
- **Accuracy**: 97.21% test accuracy

</div>
