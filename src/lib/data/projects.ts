export interface Project {
  id: string;
  title: string;
  description: string;
  image: string;
  tags: string[];
  category:
    | 'llm'
    | 'computer-vision'
    | 'nlp'
    | 'data-science'
    | 'web-dev'
    | 'all';
  demoUrl?: string;
  demoLabel?: string;
  githubUrl?: string;
  year: number;
  slug: string;
  featured?: boolean;
}

const PROJECT_IMAGE_BASE =
  'https://raw.githubusercontent.com/haipradana/pradanayahya.com/refs/heads/main/static/images/projects';

/**
 * Project list — newest first. Schema is consumed by
 * `scripts/generate_rag_data.py` (RAG ingestion). Keep field names stable.
 */
export const projects: Project[] = [
  {
    id: '14',
    title: 'BMKG-Hirup — PM2.5 Air Quality Forecasting',
    description:
      'End-to-end PM2.5 air quality forecasting system (Random Forest Regressor) deployed as a full-stack web app for BMKG Yogyakarta, alongside rainfall forecasting from climatology station data.',
    image: `${PROJECT_IMAGE_BASE}/hirup_bmkg/hirup_bmkg.png`,
    tags: ['Python', 'scikit-learn', 'FastAPI', 'React', 'Time Series'],
    category: 'data-science',
    demoUrl: 'https://bmkg-hirup.pradanayahya.com',
    githubUrl: 'https://github.com/haipradana/hirup',
    year: 2026,
    slug: 'bmkg-hirup-pm25',
  },
  {
    id: '13',
    title: 'NusaVoice — Lightweight Indonesian Text-to-Speech',
    description:
      'Lightweight Bahasa Indonesia text-to-speech model fine-tuned from Piper/VITS, with male and female voices optimized for CPU-only real-time inference.',
    image: `${PROJECT_IMAGE_BASE}/nusavoice/nusavoice.png`,
    tags: ['Piper', 'VITS', 'TTS', 'FastAPI', 'React'],
    category: 'nlp',
    demoUrl: 'https://nusavoice.pradanayahya.com',
    githubUrl: 'https://github.com/haipradana/NusaVoice',
    year: 2025,
    slug: 'nusavoice-indonesian-tts',
    featured: true,
  },
  {
    id: '12',
    title: 'Smart Space (Jarvis) — Offline Voice Assistant',
    description:
      'Local-first voice pipeline for lab automation at DTETI UGM. Whisper (ASR) + Piper (TTS, fine-tuned voice) run fully offline on a Raspberry Pi, with an LLM for command understanding and N8N for IoT control of lights, HVAC, and projectors.',
    image: `${PROJECT_IMAGE_BASE}/smartlab_jarvis/smartlab.png`,
    tags: ['Whisper', 'Piper', 'LLM', 'N8N', 'Raspberry Pi'],
    category: 'llm',
    demoUrl:
      'https://drive.google.com/file/u/1/d/15LTr5WR-MJreDqNmjXJ5QOjcOOM1l6Ez/view',
    demoLabel: 'Demo video',
    year: 2025,
    slug: 'smart-space-jarvis',
  },
  {
    id: '11',
    title: 'KawanIsyarat — Offline BISINDO Translator',
    description:
      'Android app for real-time BISINDO ↔ Indonesian translation. Runs fully on-device — built for Google’s Gemma 4 Good Hackathon.',
    image: `${PROJECT_IMAGE_BASE}/kawan_isyarat/kawan-isyarat.png`,
    tags: ['Flutter', 'MediaPipe', 'Gemma 4', 'Sign Language', 'On-device AI'],
    category: 'computer-vision',
    demoUrl: 'https://kawanisyarat.pradanayahya.com',
    githubUrl: 'https://github.com/haipradana/KawanIsyarat',
    year: 2025,
    slug: 'kawanisyarat-bisindo',
    featured: true,
  },
  {
    id: '10',
    title: 'ask-docs — Agentic RAG Assistant',
    description:
      'Production-deployed agentic RAG system live at ask.pradanayahya.com. Combines retrieval, citation, and tool-using agent loops for document-grounded Q&A.',
    image: `${PROJECT_IMAGE_BASE}/ask-docs/ask-docs.png`,
    tags: ['RAG', 'LLM', 'Agents', 'Vector Search'],
    category: 'llm',
    demoUrl: 'https://ask.pradanayahya.com',
    githubUrl: 'https://github.com/haipradana/ask-docs',
    year: 2025,
    slug: 'ask-docs-agentic-rag',
  },
  {
    id: '9',
    title: 'DINOv3 + Pseudo-labeling for Traditional Houses',
    description:
      '2nd Place at DSC LOGIKA UI 2025. Semi-supervised classification pipeline for Indonesian traditional house images using DINOv3 features and pseudo-labeling; 97.21% test accuracy.',
    image: `${PROJECT_IMAGE_BASE}/dino_logika_ui/dinov3-logika.png`,
    tags: ['DINOv3', 'Semi-supervised', 'Image Classification'],
    category: 'computer-vision',
    year: 2025,
    slug: 'dinov3-traditional-houses',
  },
  {
    id: '8',
    title: 'IndoBERT NER for Indonesian Culinary Text',
    description:
      '3rd Place at ACTION UNESA 2025 Data Mining Competition. Named Entity Recognition pipeline for Indonesian culinary text using IndoBERT; Micro-F1 0.8411 on the Kaggle leaderboard.',
    image: `${PROJECT_IMAGE_BASE}/sarcasm_indobert_1/sarcasm_indobert.jpg`,
    tags: ['NLP', 'IndoBERT', 'NER'],
    category: 'nlp',
    year: 2025,
    slug: 'indobert-culinary-ner',
  },
  {
    id: '7',
    title: 'Sentimen Analisis Abolisi Tom dan Hasto',
    description:
      'Sentiment analysis and topic modeling on public response to Prabowo’s decision granting abolition to Tom and amnesty to Hasto.',
    image: `${PROJECT_IMAGE_BASE}/abolisi_tom_hasto/tom2.jpg`,
    tags: ['NLP', 'Sentiment Analysis', 'BERTopic'],
    category: 'nlp',
    demoUrl:
      'https://x.com/haipradana/status/1951344945295663171?t=cn_0U9QgrNNQDYqveyJCYQ&s=19',
    githubUrl:
      'https://github.com/haipradana/barengdata/tree/main/Abolisi%20Tom%20Lembong',
    year: 2025,
    slug: 'sentimen-analisis-abolisi-tom-dan-hasto',
  },
  {
    id: '6',
    title: 'Sentimen Analisis Vonis Tom Lembong',
    description:
      'Sentiment analysis and topic modeling on the Tom Lembong verdict. BERT for sentiment classification and BERTopic for topic modeling.',
    image: `${PROJECT_IMAGE_BASE}/vonis_tom_lembong/thumbnailTom1.jpg`,
    tags: ['NLP', 'Sentiment Analysis', 'BERTopic'],
    category: 'nlp',
    demoUrl: 'https://www.instagram.com/p/DM72xWmPTen',
    githubUrl:
      'https://github.com/haipradana/barengdata/tree/main/Tom%20Lembong%201',
    year: 2025,
    slug: 'sentimen-analisis-vonis-tom-lembong',
  },
  {
    id: '5',
    title: 'Hate Speech Classification (RoBERTa)',
    description:
      'Fine-tuned sentiment-based RoBERTa for hate speech classification on Indonesian text.',
    image: `${PROJECT_IMAGE_BASE}/hate_classification_roberta/hate_roberta.jpg`,
    tags: ['NLP', 'RoBERTa', 'Fine-Tuning'],
    category: 'nlp',
    demoUrl:
      'https://huggingface.co/haipradana/roberta-hate-classification-model',
    githubUrl:
      'https://github.com/haipradana/RoBERTa-Indonesian-Hate-Tweet-Classification',
    year: 2025,
    slug: 'hate-speech-roberta',
  },
  {
    id: '4',
    title: 'Sarcasm Detection (IndoBERT Fine-Tuning)',
    description:
      'Fine-tuned IndoBERT base for sarcasm classification on Indonesian social-media text.',
    image: `${PROJECT_IMAGE_BASE}/sarcasm_indobert_1/sarcasm_indobert.jpg`,
    tags: ['NLP', 'IndoBERT', 'Fine-Tuning'],
    category: 'nlp',
    demoUrl:
      'https://huggingface.co/haipradana/indobert-indonesia-satire-sarcastic-classification-model',
    githubUrl:
      'https://github.com/haipradana/indobert-indonesia-sarcastic-satire-classification',
    year: 2025,
    slug: 'sarcasm-indobert',
  },
  {
    id: '3',
    title: 'TRACKO — Retail Behavior Analysis',
    description:
      'Champion at DATATHON 2025. Multimodal retail analytics platform turning ordinary CCTV footage into customer-behavior signals and strategy.',
    image: `${PROJECT_IMAGE_BASE}/datathon_2025-1/retail-behaviour-1.jpg`,
    tags: ['Computer Vision', 'TimeSformer', 'LLM'],
    category: 'computer-vision',
    demoUrl:
      'https://huggingface.co/spaces/haipradana/retail-behavior-analysis',
    githubUrl:
      'https://github.com/haipradana/DATATHON-2025-Retail-Behaviour-Analysis',
    year: 2025,
    slug: 'retail-behaviour-analysis-v1',
    featured: true,
  },
  {
    id: '2',
    title: 'Mood2Movie',
    description:
      'Movie recommendations based on your mood. Built with semantic search, sentiment analysis, and mood-based filtering.',
    image: `${PROJECT_IMAGE_BASE}/mood2movie/mood2movie.jpg`,
    tags: ['Python', 'LLM', 'Transformers', 'NLP'],
    category: 'llm',
    demoUrl: 'https://mood2movie.streamlit.app/',
    githubUrl: 'https://github.com/haipradana/Mood2Movie',
    year: 2025,
    slug: 'mood2movie',
  },
  {
    id: '1',
    title: 'ChatMyDocs',
    description:
      'RAG-based assistant that uses ModernBERT for semantic retrieval. Upload your PDFs and get precise, citation-backed answers.',
    image: `${PROJECT_IMAGE_BASE}/chatmydocs/modernbert.jpg`,
    tags: ['RAG', 'Python', 'ModernBERT'],
    category: 'llm',
    demoUrl: 'https://github.com/haipradana/ChatMyDocs',
    githubUrl: 'https://github.com/haipradana/ChatMyDocs',
    year: 2025,
    slug: 'chatmydocs',
  },
];

export const categories = [
  { id: 'all', label: 'All', count: projects.length },
  {
    id: 'llm',
    label: 'LLM & Agents',
    count: projects.filter((p) => p.category === 'llm').length,
  },
  {
    id: 'computer-vision',
    label: 'Computer Vision',
    count: projects.filter((p) => p.category === 'computer-vision').length,
  },
  {
    id: 'nlp',
    label: 'NLP',
    count: projects.filter((p) => p.category === 'nlp').length,
  },
  {
    id: 'data-science',
    label: 'Data Science',
    count: projects.filter((p) => p.category === 'data-science').length,
  },
  {
    id: 'web-dev',
    label: 'Web',
    count: projects.filter((p) => p.category === 'web-dev').length,
  },
];

export const featuredProjects = projects.filter((p) => p.featured);
