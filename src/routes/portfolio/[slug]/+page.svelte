<script lang="ts">
  import { page } from '$app/stores';
  import { projects } from '$lib/data/projects';
  import { ArrowLeft, ArrowUpRight, ExternalLink, Github, Calendar, MapPin } from 'lucide-svelte';
  import { onMount } from 'svelte';
  import { marked } from 'marked';
  import DOMPurify from 'dompurify';
  import JsonLd from '$lib/components/JsonLd.svelte';

  $: slug = $page.params.slug;
  $: project = projects.find((p) => p.slug === slug);
  $: videoEmbedUrl = project?.videoUrl ? getVideoEmbedUrl(project.videoUrl) : '';

  // Related projects in the same category, excluding self.
  $: related = project
    ? projects
        .filter((p) => p.category === project!.category && p.slug !== project!.slug)
        .slice(0, 3)
    : [];

  $: projectJsonLd = project
    ? {
        '@context': 'https://schema.org',
        '@type': 'CreativeWork',
        name: project.title,
        description: project.description,
        url: 'https://pradanayahya.com/portfolio/' + project.slug,
        image: project.image,
        dateCreated: String(project.year),
        keywords: project.tags.join(', '),
        author: {
          '@type': 'Person',
          name: 'Pradana Yahya Abdillah',
          url: 'https://pradanayahya.com',
        },
      }
    : null;

  // Try to fetch a long-form markdown writeup if one exists; fall back to
  // the structured data we already have. This loads client-side, but the
  // server-rendered page already ships substantive content (description,
  // tags, year, links, related) so Google never sees a thin page.
  let markdownHtml = '';
  function renderProjectMarkdown(md: string) {
    const html = DOMPurify.sanitize(marked.parse(md) as string);
    const template = document.createElement('template');
    template.innerHTML = html;
    template.content.querySelector('h1')?.remove();
    return template.innerHTML;
  }

  function getVideoEmbedUrl(url: string) {
    const youtubeMatch = url.match(/(?:youtu\.be\/|youtube\.com\/watch\?v=)([^&?/]+)/);
    if (youtubeMatch?.[1]) {
      return `https://www.youtube.com/embed/${youtubeMatch[1]}`;
    }

    const driveMatch = url.match(/drive\.google\.com\/file\/(?:u\/\d+\/)?d\/([^/]+)/);
    if (driveMatch?.[1]) {
      return `https://drive.google.com/file/d/${driveMatch[1]}/preview`;
    }

    return '';
  }

  onMount(async () => {
    if (!project) return;
    try {
      const res = await fetch(`/projects/${project.slug}.md`);
      if (res.ok) {
        const md = await res.text();
        markdownHtml = renderProjectMarkdown(md);
      }
    } catch {
      /* leave markdownHtml empty; the structured fallback handles it */
    }
  });

  const categoryLabel: Record<string, string> = {
    llm: 'LLM & Agents',
    'computer-vision': 'Computer Vision',
    nlp: 'NLP',
    'data-science': 'Data Science',
    'web-dev': 'Web',
    all: 'Project',
  };
</script>

<svelte:head>
  <title>{project ? `${project.title} - Pradana Yahya` : 'Project Not Found - Pradana Yahya'}</title>
  <meta name="description" content={project ? project.description : 'Project not found'} />
  {#if project}
    <meta property="og:title" content={`${project.title} - Pradana Yahya`} />
    <meta property="og:description" content={project.description} />
    <meta property="og:image" content={project.image} />
    <meta property="og:type" content="article" />
    <meta name="twitter:title" content={`${project.title} - Pradana Yahya`} />
    <meta name="twitter:description" content={project.description} />
    <meta name="twitter:image" content={project.image} />
  {:else}
    <meta name="robots" content="noindex, follow" />
  {/if}
</svelte:head>

{#if projectJsonLd}
  <JsonLd data={projectJsonLd} />
{/if}

{#if project}
  <article class="mx-auto max-w-3xl px-5 sm:px-8 pt-10 lg:pt-14 pb-20">
    <a
      href="/portfolio"
      class="inline-flex items-center gap-1.5 text-sm text-ink-muted-light dark:text-ink-muted-dark hover:text-ink-light dark:hover:text-ink-dark transition-colors"
    >
      <ArrowLeft class="h-4 w-4" /> All projects
    </a>

    <header class="mt-6">
      <div class="flex flex-wrap items-center gap-2 mb-4">
        <span class="chip-accent">{categoryLabel[project.category] ?? 'Project'}</span>
        <span class="inline-flex items-center gap-1 text-[12px] text-ink-muted-light dark:text-ink-muted-dark">
          <Calendar class="h-3 w-3" /> {project.year}
        </span>
      </div>

      <h1 class="font-display text-4xl lg:text-5xl text-ink-light dark:text-ink-dark text-balance">
        {project.title}
      </h1>

      <p class="mt-4 text-[17px] leading-relaxed text-ink-muted-light dark:text-ink-muted-dark text-pretty">
        {project.description}
      </p>

      <div class="mt-6 flex flex-wrap gap-2">
        {#if project.demoUrl}
          <a
            href={project.demoUrl}
            target="_blank"
            rel="noopener noreferrer"
            class="btn-primary"
          >
            <ExternalLink class="h-4 w-4" /> {project.demoLabel ?? 'Live demo'}
          </a>
        {/if}
        {#if project.githubUrl}
          <a
            href={project.githubUrl}
            target="_blank"
            rel="noopener noreferrer"
            class="btn-ghost"
          >
            <Github class="h-4 w-4" /> Source
          </a>
        {/if}
      </div>
    </header>

    <figure class="mt-10">
      <div class="relative overflow-hidden rounded-2xl border border-ink-faint-light dark:border-ink-faint-dark bg-surface-light-muted dark:bg-surface-dark-muted">
        <img
          src={project.image}
          alt={project.title}
          class="w-full h-auto object-cover"
          loading="eager"
          decoding="async"
        />
      </div>
    </figure>

    <!-- Overview block. Rendered server-side so the page always has useful content. -->
    <section class="mt-12">
      <h2 class="font-display text-2xl text-ink-light dark:text-ink-dark">Overview</h2>
      <p class="mt-3 text-[15px] leading-relaxed text-ink-light/85 dark:text-ink-dark/85 text-pretty">
        <strong>{project.title}</strong> is a {categoryLabel[project.category]?.toLowerCase() ?? 'project'}
        project by Pradana Yahya Abdillah, built in {project.year}. {project.description}
      </p>
    </section>

    {#if videoEmbedUrl}
      <section class="mt-8">
        <div class="overflow-hidden rounded-2xl border border-ink-faint-light bg-surface-light-muted shadow-sm dark:border-ink-faint-dark dark:bg-surface-dark-muted">
          <iframe
            src={videoEmbedUrl}
            title={`${project.title} demo video`}
            class="aspect-video w-full"
            loading="lazy"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            allowfullscreen
          ></iframe>
        </div>
      </section>
    {/if}

    <section class="mt-10 grid gap-8 sm:grid-cols-2">
      <div>
        <h3 class="text-[12px] uppercase tracking-[0.18em] text-ink-muted-light dark:text-ink-muted-dark mb-3">
          Tech stack
        </h3>
        <div class="flex flex-wrap gap-1.5">
          {#each project.tags as t}
            <span class="chip">{t}</span>
          {/each}
        </div>
      </div>

      <div>
        <h3 class="text-[12px] uppercase tracking-[0.18em] text-ink-muted-light dark:text-ink-muted-dark mb-3">
          Links
        </h3>
        <ul class="space-y-1.5 text-sm">
          {#if project.demoUrl}
            <li>
              <a
                href={project.demoUrl}
                target="_blank"
                rel="noopener noreferrer"
                class="inline-flex items-center gap-1.5 text-ink-light dark:text-ink-dark hover:text-accent-600 dark:hover:text-accent-400"
              >
                <ExternalLink class="h-3.5 w-3.5" /> {project.demoLabel ?? 'Live demo'}
              </a>
            </li>
          {/if}
          {#if project.githubUrl}
            <li>
              <a
                href={project.githubUrl}
                target="_blank"
                rel="noopener noreferrer"
                class="inline-flex items-center gap-1.5 text-ink-light dark:text-ink-dark hover:text-accent-600 dark:hover:text-accent-400"
              >
                <Github class="h-3.5 w-3.5" /> {project.githubUrl.replace(/^https?:\/\/(www\.)?/, '')}
              </a>
            </li>
          {/if}
          {#if !project.demoUrl && !project.githubUrl}
            <li class="text-ink-muted-light dark:text-ink-muted-dark">No public links yet.</li>
          {/if}
        </ul>
      </div>
    </section>

    {#if markdownHtml}
      <section class="project-markdown mt-12">
        {@html markdownHtml}
      </section>
    {/if}

    {#if related.length}
      <section class="mt-16 pt-10 border-t border-ink-faint-light dark:border-ink-faint-dark">
        <h2 class="font-display text-2xl text-ink-light dark:text-ink-dark mb-6">
          Related projects
        </h2>
        <ul class="grid gap-3 sm:grid-cols-2">
          {#each related as r}
            <li>
              <a
                href={`/portfolio/${r.slug}`}
                class="block surface rounded-xl p-4 hover:border-accent-300 dark:hover:border-accent-700 transition-colors"
              >
                <p class="text-[11px] uppercase tracking-[0.18em] text-ink-muted-light dark:text-ink-muted-dark">
                  {r.year}
                </p>
                <h3 class="font-display text-base mt-1 text-ink-light dark:text-ink-dark group-hover:text-accent-600 leading-tight">
                  {r.title}
                </h3>
                <span class="mt-2 inline-flex items-center gap-1 text-xs text-ink-muted-light dark:text-ink-muted-dark">
                  Read <ArrowUpRight class="h-3 w-3" />
                </span>
              </a>
            </li>
          {/each}
        </ul>
      </section>
    {/if}
  </article>
{:else}
  <section class="mx-auto max-w-2xl px-5 sm:px-8 py-24 text-center">
    <h1 class="font-display text-4xl text-ink-light dark:text-ink-dark">Project not found</h1>
    <p class="mt-3 text-ink-muted-light dark:text-ink-muted-dark">
      The project you’re looking for doesn’t exist or was renamed.
    </p>
    <a href="/portfolio" class="btn-primary mt-6">
      <ArrowLeft class="h-4 w-4" /> Back to all projects
    </a>
  </section>
{/if}
