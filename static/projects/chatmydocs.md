<div class="dark:text-white">

# ChatMyDocs dengan ModernBERT

## Overview

ChatMyDocs memungkinkan Anda bertanya langsung ke file PDF. Berbeda dengan LLM biasa yang bisa kehilangan konteks pada dokumen panjang, ChatMyDocs menggunakan ModernBERT untuk membuat embedding dari setiap potongan teks PDF dan menyimpannya dalam VectorStoreIndex. Saat Anda bertanya, sistem mencari potongan teks yang paling relevan, melakukan reranking dengan cross-encoder, lalu memberi jawaban dengan sumber dari bagian PDF terkait.

<center>
<a href="https://youtu.be/lETbVuimVCg" target="_blank">
<img src="https://github.com/haipradana/ChatMyDocs/blob/main/screenshot.png?raw=true" width="90%">
</a>
</center>

Sistem ini memanfaatkan ModernBERT untuk membuat embedding (representasi vektor) dari setiap potongan teks PDF, yang kemudian disimpan dalam VectorStoreIndex.  
Saat Anda mengajukan pertanyaan, sistem akan:

- Membagi PDF menjadi potongan-potongan kecil (chunk)
- Membuat embedding dari pertanyaan Anda
- Melakukan pencarian chunk yang paling relevan menggunakan similarity embedding
- Melakukan reranking hasil pencarian dengan cross-encoder agar hasil semakin presisi
- Memberikan jawaban yang dirangkum oleh LLM, lengkap dengan sumber (cite) dari bagian PDF terkait

Dengan cara ini, jawaban yang diberikan lebih relevan, dapat dicek sumbernya, dan mengurangi risiko jawaban yang tidak sesuai konteks dokumen.

## Fitur Utama

- **ModernBERT Embeddings**: Menggunakan `nomic-ai/modernbert-embed-base` untuk pencarian semantik
- **Smart Reranking**: Reranking dengan cross-encoder `cross-encoder/ms-marco-MiniLM-L-6-v2`
- **Dukungan OCR**: Ekstraksi teks otomatis dengan fallback EasyOCR
- **Streaming Responses**: respons chat bertahap dengan Gemini 2.5-flash
- **Sumber Jawaban**: Menampilkan sumber dokumen untuk setiap jawaban

## Stack

- **Frontend**: Streamlit
- **Embeddings**: ModernBERT <a href="https://huggingface.co/nomic-ai/modernbert-embed-base" target="_blank">(nomic-ai/modernbert-embed-base)</a>
- **Reranking**: Cross-encoder <a href="https://huggingface.co/cross-encoder/ms-marco-MiniLM-L-6-v2" target="_blank">(cross-encoder/ms-marco-MiniLM-L-6-v2)</a>
- **LLM**: Google Gemini 2.5-flash
- **Pemrosesan PDF**: PyPDF2 + EasyOCR (untuk pdf gambar, bukan hasil scan)
- **Vector Store**: LlamaIndex VectorStoreIndex

</div>
