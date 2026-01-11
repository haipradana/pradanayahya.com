export interface Project {
  id: string;
  title: string;
  description: string;
  image: string;
  tags: string[];
  category:
    | "llm"
    | "computer-vision"
    | "nlp"
    | "data-science"
    | "web-dev"
    | "all";
  demoUrl?: string;
  githubUrl?: string;
  year: number;
  slug: string;
}

export const projects: Project[] = [
  {
    id: "7",
    title: "Sentimen Analisis Abolisi Tom dan Hasto",
    description:
      "Sentimen analisis publik dan topic modeling pada keputusan Prabowo yang mengabulkan abolisi Tom dan amnesti Hasto.",
    image:
      "https://raw.githubusercontent.com/haipradana/pradanayahya.com/refs/heads/main/static/images/projects/abolisi_tom_hasto/tom2.jpg",
    tags: ["NLP", "Sentiment Analysis", "BERTopic"],
    category: "nlp",
    demoUrl:
      "https://x.com/haipradana/status/1951344945295663171?t=cn_0U9QgrNNQDYqveyJCYQ&s=19",
    githubUrl:
      "https://github.com/haipradana/barengdata/tree/main/Abolisi%20Tom%20Lembong",
    year: 2025,
    slug: "sentimen-analisis-abolisi-tom-dan-hasto",
  },
  {
    id: "6",
    title: "Sentimen Analisis Vonis Tom Lembong",
    description:
      "Sentimen analisis dan topic modeling pada vonis Tom Lembong, BERT untuk klasifikasi sentimen dan BertTopic untuk topic modeling.",
    image:
      "https://raw.githubusercontent.com/haipradana/pradanayahya.com/refs/heads/main/static/images/projects/vonis_tom_lembong/thumbnailTom1.jpg",
    tags: ["NLP", "Sentiment Analysis", "BERTopic"],
    category: "nlp",
    demoUrl:
      "https://www.instagram.com/p/DM72xWmPTen",
    githubUrl:
      "https://github.com/haipradana/barengdata/tree/main/Tom%20Lembong%201",
    year: 2025,
    slug: "sentimen-analisis-vonis-tom-lembong",
  },
  {
    id: "5",
    title: "Klasifikasi Hate Speech (RoBERTa)",
    description:
      "Fine-tuned RoBERTa sentiment-based model untuk klasifikasi hate speech pada teks bahasa Indonesia.",
    image:
      "https://raw.githubusercontent.com/haipradana/pradanayahya.com/refs/heads/main/static/images/projects/hate_classification_roberta/hate_roberta.jpg",
    tags: ["NLP", "RoBERTa", "Fine-Tuning"],
    category: "nlp",
    demoUrl:
      "https://huggingface.co/haipradana/roberta-hate-classification-model",
    githubUrl:
      "https://github.com/haipradana/RoBERTa-Indonesian-Hate-Tweet-Classification",
    year: 2025,
    slug: "hate-speech-roberta",
  },
  {
    id: "4",
    title: "Deteksi Sarkas (IndoBERT Fine-Tuning)",
    description:
      "Fine-tuned IndoBERT base untuk klasifikasi sarkas pada teks bahasa Indonesia, dengan dataset media sosial.",
    image:
      "https://raw.githubusercontent.com/haipradana/pradanayahya.com/refs/heads/main/static/images/projects/sarcasm_indobert_1/sarcasm_indobert.jpg",
    tags: ["NLP", "IndoBERT", "Fine-Tuning"],
    category: "nlp",
    demoUrl:
      "https://huggingface.co/haipradana/indobert-indonesia-satire-sarcastic-classification-model",
    githubUrl:
      "https://github.com/haipradana/indobert-indonesia-sarcastic-satire-classification",
    year: 2025,
    slug: "sarcasm-indobert",
  },
  {
    id: "3",
    title: "Retail Behaviour Analysis v1",
    description:
      "Sistem analisis perilaku pelanggan dari rekaman CCTV. Menggunakan computer vision dan multimodal transformer untuk memberikan strategi bisnis.",
    image:
      "https://raw.githubusercontent.com/haipradana/pradanayahya.com/refs/heads/main/static/images/projects/datathon_2025-1/retail-behaviour-1.jpg",
    tags: ["Computer Vision", "TimeSformer", "LLM"],
    category: "computer-vision",
    demoUrl:
      "https://huggingface.co/spaces/haipradana/retail-behavior-analysis",
    githubUrl:
      "https://github.com/haipradana/DATATHON-2025-Retail-Behaviour-Analysis",
    year: 2025,
    slug: "retail-behaviour-analysis-v1",
  },
  {
    id: "2",
    title: "Mood2Movie",
    description:
      "Generate movie recommendations based on your mood. Built with semantic search, sentiment analysis, and mood-based filtering.",
    image:
      "https://raw.githubusercontent.com/haipradana/pradanayahya.com/refs/heads/main/static/images/projects/mood2movie/mood2movie.jpg",
    tags: ["Python", "LLM", "Transformers", "NLP"],
    category: "llm",
    demoUrl: "https://mood2movie.streamlit.app/",
    githubUrl: "https://github.com/haipradana/Mood2Movie",
    year: 2025,
    slug: "mood2movie",
  },
  {
    id: "1",
    title: "ChatMyDocs",
    description:
      "RAG-based assistant that uses ModernBERT for semantic retrieval. Upload your PDFs and get precise, citation-backed answers.",
    image:
      "https://raw.githubusercontent.com/haipradana/pradanayahya.com/refs/heads/main/static/images/projects/chatmydocs/modernbert.jpg",
    tags: ["RAG", "Python", "ModernBERT"],
    category: "llm",
    demoUrl: "https://github.com/haipradana/ChatMyDocs",
    githubUrl: "https://github.com/haipradana/ChatMyDocs",
    year: 2025,
    slug: "chatmydocs",
  },
];

export const categories = [
  { id: "all", label: "All Projects", count: projects.length },
  {
    id: "llm",
    label: "LLM & AI",
    count: projects.filter((p) => p.category === "llm").length,
  },
  {
    id: "computer-vision",
    label: "Computer Vision",
    count: projects.filter((p) => p.category === "computer-vision").length,
  },
  {
    id: "nlp",
    label: "NLP",
    count: projects.filter((p) => p.category === "nlp").length,
  },
  {
    id: "data-science",
    label: "Data Science",
    count: projects.filter((p) => p.category === "data-science").length,
  },
  {
    id: "web-dev",
    label: "Web Development",
    count: projects.filter((p) => p.category === "web-dev").length,
  },
];
