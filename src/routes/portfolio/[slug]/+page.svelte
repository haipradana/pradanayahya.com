<script lang="ts">
  import { page } from '$app/stores';
  import { projects } from '$lib/data/projects';
  import { ArrowLeft, ExternalLink, Github, Calendar, Tag } from 'lucide-svelte';
  import { onMount } from 'svelte';

  $: slug = $page.params.slug;
  $: project = projects.find(p => p.slug === slug);

  let markdownContent = '';

  onMount(async () => {
    if (project) {
      try {
        const response = await fetch(`/projects/${project.slug}.md`);
        if (response.ok) {
          markdownContent = await response.text();
        } else {
          markdownContent = `# ${project.title}\n\n${project.description}\n\nDetailed content coming soon...`;
        }
      } catch (error) {
        markdownContent = `# ${project.title}\n\n${project.description}\n\nDetailed content coming soon...`;
      }
    }
  });

  // Simple markdown to HTML converter for basic formatting
  function parseMarkdown(text: string): string {
    return text
      .replace(/^# (.*$)/gim, '<h1 class="text-3xl font-bold mb-6 text-gray-900 dark:text-gray-100">$1</h1>')
      .replace(/^## (.*$)/gim, '<h2 class="text-2xl font-semibold mb-4 text-gray-900 dark:text-gray-100">$1</h2>')
      .replace(/^### (.*$)/gim, '<h3 class="text-xl font-semibold mb-3 text-gray-900 dark:text-gray-100">$1</h3>')
      .replace(/\*\*(.*)\*\*/gim, '<strong class="font-semibold">$1</strong>')
      .replace(/\*(.*)\*/gim, '<em class="italic">$1</em>')
      .replace(/\n\n/gim, '</p><p class="mb-4 text-gray-600 dark:text-gray-300 leading-relaxed">')
      .replace(/^(?!<h|<p)/gm, '<p class="mb-4 text-gray-600 dark:text-gray-300 leading-relaxed">')
      .replace(/$(?!<\/h|<\/p)/gm, '</p>');
  }
</script>

<svelte:head>
  <title>{project ? `${project.title} — Pradana Yahya` : 'Project Not Found — Pradana Yahya'}</title>
  <meta name="description" content={project ? project.description : 'Project not found'} />
  {#if project}
    <meta property="og:title" content={`${project.title} — Pradana Yahya`} />
    <meta property="og:description" content={project.description} />
    <meta property="og:image" content={project.image} />
    <meta property="og:type" content="article" />
    <meta name="twitter:title" content={`${project.title} — Pradana Yahya`} />
    <meta name="twitter:description" content={project.description} />
    <meta name="twitter:image" content={project.image} />
    <script type="application/ld+json">
      {JSON.stringify({
        '@context': 'https://schema.org',
        '@type': 'CreativeWork',
        name: project.title,
        description: project.description,
        url: `https://pradanayahya.com/portfolio/${project.slug}`,
        image: project.image,
        dateCreated: String(project.year),
        keywords: project.tags.join(', '),
        author: {
          '@type': 'Person',
          name: 'Pradana Yahya Abdillah',
          url: 'https://pradanayahya.com',
        },
      })}
    </script>
  {:else}
    <meta name="robots" content="noindex, follow" />
  {/if}
</svelte:head>

<div class="max-w-4xl mx-auto px-4 py-12">
  {#if project}
    <!-- Back Button -->
    <div class="mb-8">
      <a 
        href="/portfolio" 
        class="inline-flex items-center text-gray-700 dark:text-gray-300 hover:text-gray-900 dark:hover:text-gray-100 transition-colors"
      >
        <ArrowLeft class="w-4 h-4 mr-2" />
        Back to Portfolio
      </a>
    </div>

    <!-- Project Header -->
    <header class="mb-12">
      <div class="flex flex-col md:flex-row md:items-center md:justify-between mb-6">
        <h1 class="text-4xl font-bold text-gray-900 dark:text-gray-100 mb-4 md:mb-0">
          {project.title}
        </h1>
        <div class="flex items-center text-gray-500 dark:text-gray-500">
          <Calendar class="w-4 h-4 mr-2" />
          {project.year}
        </div>
      </div>

      <!-- Project Image -->
      <div class="relative rounded-lg overflow-hidden mb-6">
        <img
          src={project.image}
          alt={project.title}
          class="w-full h-64 md:h-80 object-cover"
        />
      </div>

      <!-- Project Meta -->
      <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
        <div class="flex flex-wrap gap-2">
          {#each project.tags as tag}
            <span class="inline-flex items-center px-3 py-1 text-sm font-medium bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-300 rounded-full">
              <Tag class="w-3 h-3 mr-1" />
              {tag}
            </span>
          {/each}
        </div>

        <div class="flex space-x-3">
          {#if project.demoUrl}
            <a
              href={project.demoUrl}
              target="_blank"
              rel="noopener noreferrer"
              class="inline-flex items-center px-4 py-2 bg-gray-800 hover:bg-gray-700 dark:bg-gray-200 dark:hover:bg-gray-100 text-white dark:text-gray-900 font-medium rounded-lg transition-colors"
            >
              <ExternalLink class="w-4 h-4 mr-2" />
              Live Demo
            </a>
          {/if}
          {#if project.githubUrl}
            <a
              href={project.githubUrl}
              target="_blank"
              rel="noopener noreferrer"
              class="inline-flex items-center px-4 py-2 bg-gray-100 dark:bg-gray-700 hover:bg-gray-200 dark:hover:bg-gray-600 text-gray-900 dark:text-gray-100 font-medium rounded-lg transition-colors"
            >
              <Github class="w-4 h-4 mr-2" />
              Source Code
            </a>
          {/if}
        </div>
      </div>
    </header>

    <!-- Project Content -->
    <article class="prose prose-lg dark:prose-invert max-w-none">
      {#if markdownContent}
        {@html parseMarkdown(markdownContent)}
      {:else}
        <p class="text-gray-600 dark:text-gray-100">Loading content...</p>
      {/if}
    </article>
  {:else}
    <!-- Project Not Found -->
    <div class="text-center py-16">
      <h1 class="text-4xl font-bold text-gray-900 dark:text-gray-200 mb-4">
        Project Not Found
      </h1>
      <p class="text-xl text-gray-600 dark:text-gray-400 mb-8">
        The project you're looking for doesn't exist.
      </p>
      <a 
        href="/portfolio" 
        class="inline-flex items-center px-6 py-3 bg-gray-800 hover:bg-gray-700 dark:bg-gray-200 dark:hover:bg-gray-100 text-white dark:text-gray-900 font-medium rounded-lg transition-colors"
      >
        <ArrowLeft class="w-4 h-4 mr-2" />
        Back to Portfolio
      </a>
    </div>
  {/if}
</div>