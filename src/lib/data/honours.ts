export type HonourType = 'experience' | 'award' | 'education';

export interface HonourPeriod {
  /** Display label in "Mon YYYY" format. Example: "Sep 2025". */
  from: string;
  /** Display label in "Mon YYYY" format. Omit for single-month items. */
  to?: string;
}

export interface HonourLink {
  label: string;
  url: string;
}

export interface HonourItem {
  id: string;
  type: HonourType;
  title: string;
  org?: string;
  location?: string;
  period?: HonourPeriod;
  description?: string;
  highlights?: string[];
  tags?: string[];
  links?: HonourLink[];
  /** Award placement (1 = best). Used to sort award lists. */
  rank?: number;
}

/**
 * Sort awards by best placement first (lower rank = better).
 * Items without a rank fall to the end; ties break by most recent period.
 */
export function sortAwardsByBest(items: HonourItem[]): HonourItem[] {
  return [...items].sort((a, b) => {
    const ra = a.rank ?? Number.POSITIVE_INFINITY;
    const rb = b.rank ?? Number.POSITIVE_INFINITY;
    if (ra !== rb) return ra - rb;
    return (b.period?.from ?? '').localeCompare(a.period?.from ?? '');
  });
}

/**
 * Timeline items — chronological (oldest → newest).
 * Schema is consumed by `scripts/generate_rag_data.py` (RAG ingestion),
 * so keep field names (`id`, `type`, `title`, `org`, `period.from/to`,
 * `description`, `tags`) intact.
 */
export const honours: HonourItem[] = [
  // ── Education ───────────────────────────────────────────────────────────
  {
    id: 'edu-ugm-information-technology',
    type: 'education',
    title: 'B.Sc. in Information Technology',
    org: 'Universitas Gadjah Mada',
    location: 'Yogyakarta, Indonesia',
    period: { from: 'Aug 2023', to: 'Present' },
    description:
      'Undergraduate student at the Faculty of Engineering, focusing on machine learning, computer vision, and on-device AI systems. Current GPA 3.44.',
    tags: ['Education'],
  },

  // ── Experience (oldest → newest) ────────────────────────────────────────
  {
    id: 'exp-night-login-community',
    type: 'experience',
    title: 'Data Science Member',
    org: 'Night Login Community (NDSC) — UGM',
    location: 'Yogyakarta, Indonesia',
    period: { from: 'Mar 2024', to: 'Mar 2025' },
    description:
      'Built ML models and collaborated on data preprocessing, feature engineering, and evaluation across multiple study projects within the data science division.',
    tags: ['Machine Learning', 'Data Science'],
  },
  {
    id: 'exp-fukuro-cv-programmer',
    type: 'experience',
    title: 'Computer Vision Programmer — FUKURO',
    org: 'Gadjah Mada Robotic Team (GMRT)',
    location: 'Yogyakarta, Indonesia',
    period: { from: 'Oct 2024', to: 'Present' },
    description:
      'Develop image processing algorithms for an omnidirectional 360° vision system used in wheeled soccer robots, plus real-time object detection and tracking for in-match decision making.',
    tags: ['Computer Vision', 'OpenCV', 'ROS2', 'C++'],
  },
  {
    id: 'exp-fukuro-captain',
    type: 'experience',
    title: 'Team Captain — FUKURO (KRSBI Wheeled)',
    org: 'Gadjah Mada Robotic Team (GMRT)',
    location: 'Yogyakarta, Indonesia',
    period: { from: 'Sep 2025', to: 'Present' },
    description:
      'Lead the wheeled soccer robot team for the national KRSBI competition, coordinating hardware and software divisions. Qualified to represent UGM at RoboCup 2026 in Incheon, South Korea.',
    tags: ['Leadership', 'Robotics'],
  },
  {
    id: 'exp-datains-ai-engineer-intern',
    type: 'experience',
    title: 'AI Engineer Intern',
    org: 'DataIns — PT Global Data Inspirasi',
    location: 'Yogyakarta, Indonesia',
    period: { from: 'Oct 2025', to: 'Dec 2025' },
    description:
      'Built the “Smart Space” (Jarvis) voice assistant for laboratory automation at DTETI UGM: local-first ASR/TTS pipeline (Whisper + Piper) running fully offline on Raspberry Pi, with a fine-tuned custom Piper voice, integrated with an LLM and N8N for IoT workflow control over lab devices.',
    tags: ['Whisper', 'Piper', 'LLM', 'N8N', 'Raspberry Pi'],
  },
  {
    id: 'exp-research-assistant',
    type: 'experience',
    title: 'Research Assistant — Smart Lab & Smart Space',
    org: 'DTETI, Universitas Gadjah Mada',
    location: 'Yogyakarta, Indonesia',
    period: { from: 'Dec 2025', to: 'Present' },
    description:
      'Research on AI + IoT systems for Smart Lab & Smart Space. Developed NusaVoice, a fine-tuned on-device LLM for Indonesian intent detection, with a dual-response architecture that produces both a natural-language reply and a structured tool call in a single pass.',
    tags: ['PyTorch', 'Hugging Face', 'PEFT/LoRA', 'Home Assistant'],
  },
  {
    id: 'exp-bmkg-intern',
    type: 'experience',
    title: 'Machine Learning Intern',
    org: 'BMKG — Badan Meteorologi, Klimatologi, dan Geofisika',
    location: 'Yogyakarta, Indonesia',
    period: { from: 'Dec 2025', to: 'Jan 2026' },
    description:
      'Developed an end-to-end PM2.5 air quality forecasting system (Random Forest) deployed as a full-stack web app (bmkg-hirup.pradanayahya.com), rainfall forecasting models from climatology station data, and internal digitalization tools that streamlined administrative workflows for BMKG staff.',
    tags: ['scikit-learn', 'FastAPI', 'React', 'Docker', 'Time Series'],
  },

  // ── Awards (oldest → newest) ────────────────────────────────────────────
  {
    id: 'award-datathon-2024-ristek',
    type: 'award',
    rank: 11,
    title: 'Top 11 — DATATHON 2024',
    org: 'RISTEK Fasilkom Universitas Indonesia',
    location: 'Jakarta, Indonesia',
    period: { from: 'Jul 2024' },
    description:
      'Ranked 11th out of 200+ teams. Built Graph Neural Network (GNN) models for fraud detection on a fintech transaction graph.',
    tags: ['GNN', 'PyTorch Geometric', 'Fraud Detection'],
  },
  {
    id: 'award-datavidia-arkavidia-2025',
    type: 'award',
    rank: 11,
    title: 'Top 11 — Datavidia 9, Arkavidia ITB',
    org: 'Institut Teknologi Bandung',
    location: 'Bandung, Indonesia',
    period: { from: 'Mar 2025' },
    description:
      'Ranked 11th of 230 teams with a SARIMAX-based forecasting model for Indonesian food commodity prices; moved from rank 20 → 11 with domain-specific feature engineering and a submitted technical paper.',
    tags: ['Time Series', 'SARIMAX', 'Forecasting'],
  },
  {
    id: 'award-datathon-2025-1st',
    type: 'award',
    rank: 1,
    title: 'Champion — DATATHON 2025',
    org: 'RISTEK Fasilkom Universitas Indonesia',
    location: 'Jakarta, Indonesia',
    period: { from: 'Sep 2025' },
    description:
      '1st Place with TRACKO, a multimodal retail analytics platform extracting customer behavior signals from standard CCTV footage.',
    tags: ['Computer Vision', 'Multimodal', 'TimeSformer'],
  },
  {
    id: 'award-action-unesa-3rd',
    type: 'award',
    rank: 3,
    title: '3rd Place — Data Mining Competition, ACTION UNESA 2025',
    org: 'Universitas Negeri Surabaya',
    location: 'Surabaya, Indonesia',
    period: { from: 'Nov 2025' },
    description:
      'IndoBERT-based NER pipeline for Indonesian culinary text; Micro-F1 0.8411 on the Kaggle leaderboard.',
    tags: ['NLP', 'IndoBERT', 'NER'],
  },
  {
    id: 'award-logika-ui-2025-2nd',
    type: 'award',
    rank: 2,
    title: '2nd Place — DSC LOGIKA UI 2025',
    org: 'Universitas Indonesia',
    location: 'Jakarta, Indonesia',
    period: { from: 'Nov 2025' },
    description:
      'DINOv3 + pseudo-labeling pipeline for Indonesian traditional house classification; final test accuracy 97.21%.',
    tags: ['Computer Vision', 'DINOv3', 'Semi-supervised'],
  },
];
