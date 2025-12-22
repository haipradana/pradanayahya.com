export type HonourType = 'experience' | 'award' | 'education';

export interface HonourPeriod {
  /**
   * Display label in "Mon YYYY" format.
   * Example: "Sep 2025"
   */
  from: string;
  /**
   * Display label in "Mon YYYY" format.
   * If omitted, UI can treat it as a single-month item.
   */
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
  period?: HonourPeriod;
  description?: string;
  highlights?: string[];
  tags?: string[];
  links?: HonourLink[];
}

/**
 * Timeline items (old -> new). Some periods are left empty if unknown.
 * You can fill missing periods later using "Mon YYYY" labels.
 */
export const honours: HonourItem[] = [
  {
    id: 'edu-ugm-information-engineering',
    type: 'education',
    title: 'Teknologi Informasi (S1)',
    org: 'Universitas Gadjah Mada (UGM)',
    period: { from: '2023', to: 'Now' },
    description: 'Undergraduate study in Information Engineering.',
    tags: ['Education'],
  },
  {
    id: 'exp-fukuro-cv-programmer',
    type: 'experience',
    title: 'Computer Vision Programmer of FUKURO',
    org: 'Gadjah Mada Robotic Team (GMRT)',
    period: { from: 'Nov 2024', to: 'now' },
    description:
      'Menghandle tugas vision dengan kamera 360 derajat sebagai mata robot untuk memahami posisinya dan mengetahui posisi musuh, kawan, dan bola',
    tags: ['Computer Vision', 'Team'],
  },
  {
    id: 'exp-fukuro-captain',
    type: 'experience',
    title: 'Captain FUKURO (KRSBI-Beroda)',
    org: 'Gadjah Mada Robotic Team (GMRT)',
    period: { from: 'Oct 2025', to: 'now' },
    description:
      'Sebagai kapten yang memimpin tim robotik sepakbola beroda milik UGM.',
    tags: ['Leadership', 'Team'],
  },
  {
    id: 'award-datathon-2025-1st',
    type: 'award',
    title: 'Juara 1 DATATHON 2025',
    org: 'RISTEK Universitas Indonesia',
    period: { from: 'June 2025', to: 'Sep 2025' },
    description:
      'Memenangkan kompetisi DATATHON 2025 dengan proyek TRACKO, platform untuk analisis toko retail dengan computer vision memanfaatkan CCTV sederhana',
  },
  {
    id: 'exp-datains-ai-engineer-intern',
    type: 'experience',
    title: 'AI Engineer Intern',
    org: 'DataIns',
    period: { from: 'Sep 2025', to: 'Dec 2025' },
    description:
      'Sebagai AI Engineer intern topik smart space. Menerapkan end-to-end sistem asisten suara cerdas untuk mengontrol IoT dan RAG dengan automation workflow N8N',
    tags: ['TTS', 'STT', 'AI'],
  },
  {
    id: 'award-action-unesa-3rd',
    type: 'award',
    title: 'Juara 3 Data Mining ACTION',
    org: 'Universitas Negeri Surabaya',
    period: { from: 'Nov 2025', to: 'Nov 2025' },
    description:
      'Mendapatkan juara 3 dalam cabang lomba Data Mining di ACTION UNESA.',
    tags: ['Competition', 'Award'],
  },
  {
    id: 'award-logika-ui-2025-2nd',
    type: 'award',
    title: 'Juara 2 DSC LOGIKA UI 2025',
    org: 'Universitas Indonesia',
    period: { from: 'Nov 2025', to: 'Nov 2025' },
    description:
      'Mendapatkan juara 2 dalam Data Science Competition (DSC) LOGIKA UI 2025.',
    tags: ['Competition', 'Award'],
  },
  {
    id: 'exp-research-assistant',
    type: 'experience',
    title: 'Research Assistant',
    org: 'Universitas Gadjah Mada (UGM)',
    period: { from: 'Dec 2025', to: 'Now' },
    description:
      'Asisten Peneliti di Departemen Teknik Elektro dan Teknologi Informasi UGM (DTETI) dengan topik Smart Lab & Space',
    tags: ['Research', 'Assistant'],
  },
  {
    id: 'exp-bmkg-intern',
    type: 'experience',
    title: 'Machine Learning Intern',
    org: 'BMKG',
    period: { from: 'Dec 2025', to: 'Now' },
    description:
      'Internship di BMKG Stasiun Klimatologi Yogyakarta.',
    tags: ['Internship'],
  },
];

