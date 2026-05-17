<script lang="ts">
  import { projects, categories } from '$lib/data/projects';
  import ProjectCard from '$lib/components/ProjectCard.svelte';

  let selectedCategory: string = 'all';

  $: visibleCategories = categories.filter((c) => c.count > 0);
  $: filtered =
    selectedCategory === 'all'
      ? projects
      : projects.filter((p) => p.category === selectedCategory);
</script>

<svelte:head>
  <title>Projects - Pradana Yahya</title>
  <meta name="description" content="A catalog of AI, ML, and software projects by Pradana Yahya." />
</svelte:head>

<section class="mx-auto max-w-6xl px-5 sm:px-8 pt-14 lg:pt-20 pb-10">
  <p class="eyebrow">Projects</p>
  <h1 class="font-display text-4xl lg:text-5xl mt-3 text-ink-light dark:text-ink-dark text-balance">
    A catalog of what I’ve been building.
  </h1>
  <p class="mt-4 max-w-2xl text-[15px] leading-relaxed text-ink-muted-light dark:text-ink-muted-dark">
    Research prototypes, hackathon winners, and deployed products, sorted
    by recency. Click any tile to read more.
  </p>
</section>

<section class="mx-auto max-w-6xl px-5 sm:px-8 pb-6">
  <div class="flex flex-wrap items-center gap-2">
    {#each visibleCategories as category}
      {@const active = selectedCategory === category.id}
      <button
        type="button"
        on:click={() => (selectedCategory = category.id)}
        class="inline-flex items-center gap-1.5 rounded-full px-3.5 py-1.5 text-xs font-medium transition-all border {active ? 'bg-ink-light text-surface-light border-ink-light dark:bg-ink-dark dark:text-surface-dark dark:border-ink-dark' : 'border-ink-faint-light dark:border-ink-faint-dark text-ink-muted-light dark:text-ink-muted-dark hover:text-ink-light dark:hover:text-ink-dark'}"
      >
        {category.label}
        <span class="text-[10px] opacity-70">{category.count}</span>
      </button>
    {/each}
  </div>
</section>

<section class="mx-auto max-w-6xl px-5 sm:px-8 pb-24">
  <div class="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
    {#each filtered as project (project.id)}
      <ProjectCard {project} />
    {/each}
  </div>

  {#if filtered.length === 0}
    <div class="surface rounded-2xl py-20 text-center">
      <p class="text-ink-muted-light dark:text-ink-muted-dark">
        No projects in this category yet.
      </p>
    </div>
  {/if}
</section>
