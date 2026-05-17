<script lang="ts">
  import {
    ArrowUpRight,
    MapPin,
    Github,
    Linkedin,
    Mail,
    Twitter,
  } from 'lucide-svelte';
  import HeroCarousel from '$lib/components/HeroCarousel.svelte';
  import ProjectCard from '$lib/components/ProjectCard.svelte';
  import JsonLd from '$lib/components/JsonLd.svelte';
  import { projects } from '$lib/data/projects';
  import { honours, sortAwardsByBest } from '$lib/data/honours';

  // Hero photo carousel. Drop additional files into /static/images/hero/
  // and append them here to extend the slideshow.
  const heroPhotos = [
    { src: '/images/profile.webp', alt: 'Pradana Yahya', caption: 'Yogyakarta, ID' },
    // { src: '/images/hero/hackathon.webp', alt: 'DATATHON 2025', caption: 'DATATHON 2025 Champion' },
    // { src: '/images/hero/fukuro.webp',    alt: 'GMRT FUKURO', caption: 'FUKURO RoboCup 2026' },
    // { src: '/images/hero/bmkg.webp',      alt: 'BMKG intern', caption: 'BMKG Yogyakarta' },
  ];

  // Featured: TRACKO, KawanIsyarat, NusaVoice
  const featuredSlugs = [
    'retail-behaviour-analysis-v1',
    'kawanisyarat-bisindo',
    'nusavoice-indonesian-tts',
  ];
  const featured = featuredSlugs
    .map((s) => projects.find((p) => p.slug === s))
    .filter((p): p is NonNullable<typeof p> => Boolean(p));

  const featuredAwards = sortAwardsByBest(
    honours.filter((h) => h.type === 'award')
  ).slice(0, 4);

  // Professional experiences, newest first (education excluded).
  const allExperiences = honours.filter((h) => h.type === 'experience').reverse();
  const EXPERIENCE_VISIBLE = 3;
  let experiencesExpanded = false;
  $: visibleExperiences = experiencesExpanded
    ? allExperiences
    : allExperiences.slice(0, EXPERIENCE_VISIBLE);

  const skillGroups: { title: string; items: string[] }[] = [
    {
      title: 'Programming Languages',
      items: ['Python', 'TypeScript / JavaScript', 'C / C++', 'Java', 'SQL'],
    },
    {
      title: 'Machine Learning & AI',
      items: [
        'PyTorch',
        'TensorFlow / TFLite',
        'Hugging Face',
        'PEFT / LoRA',
        'scikit-learn',
        'Pandas',
      ],
    },
    {
      title: 'NLP & LLM',
      items: ['IndoBERT', 'RoBERTa', 'BERTopic', 'RAG', 'Agents', 'Whisper · Piper'],
    },
    {
      title: 'Computer Vision',
      items: ['OpenCV', 'TimeSformer', 'DINOv3', 'ROS2', 'TFLite on-device'],
    },
    {
      title: 'Frontend',
      items: ['React', 'Next.js', 'SvelteKit', 'Tailwind CSS'],
    },
    {
      title: 'Backend & Data',
      items: ['FastAPI', 'Flask', 'Node.js', 'PostgreSQL', 'MongoDB'],
    },
    {
      title: 'DevOps & Cloud',
      items: ['Docker', 'Git', 'Azure', 'Home Assistant', 'N8N'],
    },
    {
      title: 'Hardware',
      items: ['Raspberry Pi', 'Edge devices'],
    },
  ];

  const socials = [
    { href: 'https://github.com/haipradana', label: 'GitHub', icon: Github },
    { href: 'https://linkedin.com/in/pradana-yahya', label: 'LinkedIn', icon: Linkedin },
    { href: 'https://x.com/haipradana', label: 'Twitter / X', icon: Twitter },
    { href: 'mailto:pradana@pradanayahya.com', label: 'Email', icon: Mail },
  ];

  const stats = [
    { label: 'Production deployments', value: '4+' },
    { label: 'Competition podiums', value: '3' },
    { label: 'Years building AI', value: '3' },
  ];

  const homeJsonLd = {
    '@context': 'https://schema.org',
    '@graph': [
      {
        '@type': 'ProfilePage',
        '@id': 'https://pradanayahya.com/#profile',
        url: 'https://pradanayahya.com/',
        name: 'Pradana Yahya Abdillah - AI Engineer & Data Scientist',
        mainEntity: { '@id': 'https://pradanayahya.com/#person' },
        inLanguage: 'en',
      },
      {
        '@type': 'Person',
        '@id': 'https://pradanayahya.com/#person',
        name: 'Pradana Yahya Abdillah',
        alternateName: ['Dana', 'haipradana'],
        url: 'https://pradanayahya.com',
      },
      {
        '@type': 'BreadcrumbList',
        itemListElement: [
          { '@type': 'ListItem', position: 1, name: 'Home', item: 'https://pradanayahya.com/' },
          { '@type': 'ListItem', position: 2, name: 'Projects', item: 'https://pradanayahya.com/portfolio' },
          { '@type': 'ListItem', position: 3, name: 'Experience', item: 'https://pradanayahya.com/experience' },
          { '@type': 'ListItem', position: 4, name: 'Awards', item: 'https://pradanayahya.com/awards' },
          { '@type': 'ListItem', position: 5, name: 'Writings', item: 'https://pradanayahya.com/blogs' },
          { '@type': 'ListItem', position: 6, name: 'Contact', item: 'https://pradanayahya.com/contact' },
        ],
      },
      {
        '@type': 'ItemList',
        name: 'Featured projects',
        itemListElement: featured.map((p, i) => ({
          '@type': 'ListItem',
          position: i + 1,
          url: 'https://pradanayahya.com/portfolio/' + p.slug,
          name: p.title,
        })),
      },
    ],
  };
</script>

<svelte:head>
  <title>Pradana Yahya Abdillah - AI Engineer & Data Scientist</title>
  <meta
    name="description"
    content="Pradana Yahya Abdillah (Dana) is an AI engineer and data scientist at Universitas Gadjah Mada, building projects across NLP, computer vision, RAG, and on-device AI. Champion of DATATHON 2025."
  />
</svelte:head>

<JsonLd data={homeJsonLd} />

<!-- ─── Hero ─────────────────────────────────────────────────────────────── -->
<section class="relative">
  <div class="hero-wash pointer-events-none absolute inset-0 -z-10">
    <div class="absolute top-[12%] right-[6%] h-[360px] w-[360px] rounded-full bg-accent-200/10 dark:bg-accent-500/4 blur-3xl"></div>
    <div class="absolute top-[40%] left-[2%] h-[280px] w-[280px] rounded-full bg-amber-200/10 dark:bg-amber-500/3 blur-3xl"></div>
  </div>

  <div class="mx-auto max-w-5xl px-5 sm:px-8 pt-8 md:pt-12 pb-12 md:pb-16">
    <div class="grid gap-8 md:grid-cols-12 md:gap-8 lg:gap-10 items-center">
      <div class="md:col-span-7 lg:col-span-8 animate-fade-up">
        <div class="inline-flex flex-wrap items-center gap-2 mb-4">
          <span class="inline-flex items-center gap-1.5 text-ink-muted-light dark:text-ink-muted-dark">
            <MapPin class="h-3.5 w-3.5" />
            <span class="text-xs tracking-wide">Yogyakarta, Indonesia</span>
          </span>
          <span class="chip-accent">Open to opportunities</span>
        </div>

        <h1 class="font-display text-[clamp(2rem,4.4vw,3.2rem)] font-medium leading-[1.05] text-ink-light dark:text-ink-dark text-balance max-w-[14ch]">
          Welcome, I’m
          <span class="italic text-accent-600 dark:text-accent-400">Dana</span>.
        </h1>

        <p class="mt-3 text-[15px] text-ink-muted-light dark:text-ink-muted-dark">
          AI Engineer · Data Scientist
        </p>

        <p class="mt-5 max-w-md text-[14.5px] leading-relaxed text-ink-light/85 dark:text-ink-dark/85 text-pretty">
          Third-year <strong class="font-semibold">Information Technology</strong>
          student at <strong class="font-semibold">Universitas Gadjah Mada</strong>,
          passionate about <em>computer vision</em>, <em>NLP</em>, and
          <em>on-device AI</em>.
        </p>

        <div class="mt-6 flex flex-wrap items-center gap-2">
          <a href="/portfolio" class="btn-primary">
            See projects
            <ArrowUpRight class="h-4 w-4" />
          </a>
          <a href="/experience" class="btn-ghost">Experience</a>

          <span class="hidden sm:inline-block mx-1 h-5 w-px bg-ink-faint-light dark:bg-ink-faint-dark"></span>

          <div class="flex items-center gap-1">
            {#each socials as s}
              <a
                href={s.href}
                target={s.href.startsWith('http') ? '_blank' : undefined}
                rel="noopener noreferrer"
                aria-label={s.label}
                title={s.label}
                class="inline-flex h-9 w-9 items-center justify-center rounded-full border border-ink-faint-light dark:border-ink-faint-dark text-ink-muted-light dark:text-ink-muted-dark hover:text-ink-light dark:hover:text-ink-dark hover:bg-surface-light-muted dark:hover:bg-surface-dark-muted transition-colors"
              >
                <svelte:component this={s.icon} class="h-4 w-4" />
              </a>
            {/each}
          </div>
        </div>

        <div class="mt-8 hidden sm:grid grid-cols-3 gap-4 max-w-md">
          {#each stats as s}
            <div>
              <div class="font-display text-xl text-ink-light dark:text-ink-dark">{s.value}</div>
              <div class="mt-1 text-[10px] uppercase tracking-[0.18em] text-ink-muted-light dark:text-ink-muted-dark">
                {s.label}
              </div>
            </div>
          {/each}
        </div>
      </div>

      <div
        class="md:col-span-5 lg:col-span-4 animate-fade-up w-full max-w-[11rem] sm:max-w-[14rem] mx-auto md:max-w-none md:ml-auto"
        style="animation-delay:120ms"
      >
        <HeroCarousel images={heroPhotos} interval={5500} />
      </div>
    </div>
  </div>
</section>

<!-- ─── About ────────────────────────────────────────────────────────────── -->
<section class="mx-auto max-w-5xl px-5 sm:px-8 py-14">
  <div class="grid gap-10 lg:grid-cols-12">
    <div class="lg:col-span-4">
      <p class="eyebrow">01 - About</p>
      <h2 class="font-display text-3xl lg:text-4xl mt-3 text-ink-light dark:text-ink-dark">
        Curious by default, shipping by habit.
      </h2>
    </div>
    <div class="lg:col-span-8 space-y-5 text-[15px] leading-relaxed text-ink-light/85 dark:text-ink-dark/85">
      <p>
        I like building AI systems that move from experiments into real use:
        fine-tuning small models that run on a Raspberry Pi, building RAG pipelines
        that need reliable answers, and training vision systems for robot soccer.
      </p>
      <p>
        Recent work includes an offline BISINDO translator for the Tuli community
        (<a class="underline decoration-accent-500 underline-offset-4" href="/portfolio/kawanisyarat-bisindo">KawanIsyarat</a>),
        a multimodal retail-analytics platform that won DATATHON 2025
        (<a class="underline decoration-accent-500 underline-offset-4" href="/portfolio/retail-behaviour-analysis-v1">TRACKO</a>),
        and a lightweight Indonesian text-to-speech model
        (<a class="underline decoration-accent-500 underline-offset-4" href="/portfolio/nusavoice-indonesian-tts">NusaVoice</a>).
      </p>
      <p>
        Outside the terminal, I hike, play football, and lead
        <strong>Gadjah Mada Robotic Team - FUKURO</strong>, which qualified for
        RoboCup 2026 in Incheon, South Korea.
      </p>
    </div>
  </div>
</section>

<!-- ─── Featured projects ───────────────────────────────────────────────── -->
<section class="mx-auto max-w-5xl px-5 sm:px-8 py-12">
  <div class="flex items-end justify-between mb-8 gap-4">
    <div>
      <p class="eyebrow">02 - Selected work</p>
      <h2 class="font-display text-3xl lg:text-4xl mt-3 text-ink-light dark:text-ink-dark">
        Featured projects.
      </h2>
    </div>
    <a href="/portfolio" class="hidden sm:inline-flex items-center gap-1 text-sm font-medium text-ink-muted-light dark:text-ink-muted-dark hover:text-ink-light dark:hover:text-ink-dark transition-colors">
      All projects <ArrowUpRight class="h-4 w-4" />
    </a>
  </div>

  <div class="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
    {#each featured as project}
      <ProjectCard {project} />
    {/each}
  </div>

  <div class="mt-8 flex justify-center sm:hidden">
    <a href="/portfolio" class="btn-ghost">
      All projects <ArrowUpRight class="h-4 w-4" />
    </a>
  </div>
</section>

<!-- ─── Experience ──────────────────────────────────────────────────────── -->
<section class="mx-auto max-w-5xl px-5 sm:px-8 py-12">
  <div class="flex items-end justify-between mb-8 gap-4">
    <div>
      <p class="eyebrow">03 - Experience</p>
      <h2 class="font-display text-3xl lg:text-4xl mt-3 text-ink-light dark:text-ink-dark">
        Where I’ve been.
      </h2>
    </div>
    <a
      href="/experience"
      class="hidden sm:inline-flex items-center gap-1 text-sm font-medium text-ink-muted-light dark:text-ink-muted-dark hover:text-ink-light dark:hover:text-ink-dark transition-colors"
    >
      Full timeline <ArrowUpRight class="h-4 w-4" />
    </a>
  </div>

  <ol class="relative border-l border-ink-faint-light dark:border-ink-faint-dark">
    {#each visibleExperiences as item (item.id)}
      <li class="relative grid gap-x-6 gap-y-2 grid-cols-12 py-6">
        <span
          class="absolute -left-[5px] top-7 inline-block h-2.5 w-2.5 rounded-full bg-surface-light dark:bg-surface-dark ring-2 ring-accent-500"
          aria-hidden="true"
        ></span>

        <div class="col-span-12 sm:col-span-3 pl-6">
          {#if item.period}
            <p class="text-[11px] uppercase tracking-[0.18em] text-ink-muted-light dark:text-ink-muted-dark">
              {item.period.from}{#if item.period.to && item.period.to !== item.period.from} - {item.period.to}{/if}
            </p>
          {/if}
          {#if item.location}
            <p class="mt-1 text-[12px] text-ink-muted-light/80 dark:text-ink-muted-dark/80">
              {item.location}
            </p>
          {/if}
        </div>

        <div class="col-span-12 sm:col-span-9 sm:pl-0 pl-6">
          <h3 class="font-display text-lg lg:text-xl text-ink-light dark:text-ink-dark leading-snug">
            {item.title}
          </h3>
          {#if item.org}
            <p class="mt-1 text-sm font-medium text-ink-light/80 dark:text-ink-dark/80">
              {item.org}
            </p>
          {/if}
          {#if item.description}
            <p class="mt-2 text-[14px] leading-relaxed text-ink-muted-light dark:text-ink-muted-dark text-pretty">
              {item.description}
            </p>
          {/if}
          {#if item.tags?.length}
            <div class="mt-3 flex flex-wrap gap-1.5">
              {#each item.tags.slice(0, 4) as t}
                <span class="chip">{t}</span>
              {/each}
            </div>
          {/if}
        </div>
      </li>
    {/each}
  </ol>

  {#if allExperiences.length > EXPERIENCE_VISIBLE}
    <div class="mt-6 flex justify-center">
      <button
        type="button"
        on:click={() => (experiencesExpanded = !experiencesExpanded)}
        class="btn-ghost"
        aria-expanded={experiencesExpanded}
      >
        {#if experiencesExpanded}
          Show less
        {:else}
          Load more
          <span class="text-[11px] text-ink-muted-light dark:text-ink-muted-dark">
            (+{allExperiences.length - EXPERIENCE_VISIBLE})
          </span>
        {/if}
      </button>
    </div>
  {/if}
</section>

<!-- ─── Skills & Awards (2-col on desktop, stacked on mobile) ───────────── -->
<section class="mx-auto max-w-5xl px-5 sm:px-8 py-14">
  <div class="grid gap-12 lg:grid-cols-12">
    <!-- Technical Skills -->
    <div class="lg:col-span-8">
      <p class="eyebrow">04 - Toolbox</p>
      <h2 class="font-display text-3xl lg:text-4xl mt-3 text-ink-light dark:text-ink-dark">
        Technical Skills.
      </h2>

      <div class="mt-8 grid gap-x-8 gap-y-7 sm:grid-cols-2">
        {#each skillGroups as group}
          <div class="border-l-2 border-accent-500/70 pl-4">
            <h3 class="text-[12px] font-semibold uppercase tracking-[0.14em] text-ink-light dark:text-ink-dark">
              {group.title}
            </h3>
            <div class="mt-3 flex flex-wrap gap-1.5">
              {#each group.items as item}
                <span class="chip">{item}</span>
              {/each}
            </div>
          </div>
        {/each}
      </div>
    </div>

    <!-- Latest Awards -->
    <aside class="lg:col-span-4">
      <div class="flex items-end justify-between gap-3">
        <div>
          <p class="eyebrow">05 - Recognition</p>
          <h2 class="font-display text-3xl lg:text-4xl mt-3 text-ink-light dark:text-ink-dark">
            Latest Awards.
          </h2>
        </div>
        <a
          href="/awards"
          class="hidden lg:inline-flex items-center gap-1 text-xs font-medium text-ink-muted-light dark:text-ink-muted-dark hover:text-ink-light dark:hover:text-ink-dark transition-colors"
        >
          All <ArrowUpRight class="h-3.5 w-3.5" />
        </a>
      </div>

      <ol class="mt-8 space-y-6 border-l border-ink-faint-light dark:border-ink-faint-dark pl-5">
        {#each featuredAwards as a}
          <li>
            <p class="text-[11px] uppercase tracking-[0.18em] text-ink-muted-light dark:text-ink-muted-dark">
              {a.period?.from ?? ''}
            </p>
            <h3 class="font-display text-[17px] leading-snug mt-1 text-ink-light dark:text-ink-dark">
              {a.title}
            </h3>
            {#if a.org}
              <p class="mt-1 text-[13px] text-ink-muted-light dark:text-ink-muted-dark">
                {a.org}
              </p>
            {/if}
          </li>
        {/each}
      </ol>

      <a
        href="/awards"
        class="mt-8 lg:hidden inline-flex items-center gap-1 text-sm font-medium text-ink-muted-light dark:text-ink-muted-dark hover:text-ink-light dark:hover:text-ink-dark transition-colors"
      >
        All awards <ArrowUpRight class="h-4 w-4" />
      </a>
    </aside>
  </div>
</section>

<style>
  /* Fade the ambient hero wash to transparent at the bottom. */
  .hero-wash {
    -webkit-mask-image: linear-gradient(
      to bottom,
      black 0%,
      black 55%,
      transparent 100%
    );
    mask-image: linear-gradient(
      to bottom,
      black 0%,
      black 55%,
      transparent 100%
    );
  }
</style>
