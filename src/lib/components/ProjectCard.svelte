<script lang="ts">
  import type { Project } from '$lib/data/projects';
  import { ArrowUpRight, Github } from 'lucide-svelte';

  export let project: Project;
  export let compact = false;
</script>

<article
  class="group relative flex flex-col overflow-hidden rounded-2xl border border-ink-faint-light dark:border-ink-faint-dark bg-surface-light-elev dark:bg-surface-dark-elev transition-all duration-300 hover:-translate-y-0.5 hover:shadow-[0_25px_50px_-25px_rgba(0,0,0,0.18)] dark:hover:shadow-[0_25px_50px_-15px_rgba(0,0,0,0.6)]"
>
  <a
    href={`/portfolio/${project.slug}`}
    class="block relative overflow-hidden aspect-[16/10] bg-surface-light-muted dark:bg-surface-dark-muted"
    aria-label={project.title}
  >
    <img
      src={project.image}
      alt={project.title}
      loading="lazy"
      decoding="async"
      class="absolute inset-0 h-full w-full object-cover transition-transform duration-[900ms] ease-out group-hover:scale-[1.04]"
    />
    <div class="absolute inset-0 bg-gradient-to-t from-black/30 via-transparent to-transparent opacity-60 group-hover:opacity-80 transition-opacity"></div>
    <div class="absolute top-3 left-3 flex gap-1.5">
      <span class="inline-flex items-center gap-1 rounded-full bg-white/85 backdrop-blur text-[10px] uppercase tracking-[0.18em] font-semibold text-ink-light px-2 py-1">
        {project.year}
      </span>
    </div>
  </a>

  <div class="flex flex-1 flex-col p-5">
    <h3 class="font-display text-lg leading-tight text-ink-light dark:text-ink-dark">
      <a href={`/portfolio/${project.slug}`} class="hover:underline decoration-accent-500 underline-offset-4">
        {project.title}
      </a>
    </h3>

    {#if !compact}
      <p class="mt-2 text-sm leading-relaxed text-ink-muted-light dark:text-ink-muted-dark text-pretty">
        {project.description}
      </p>
    {/if}

    <div class="mt-4 flex flex-wrap gap-1.5">
      {#each project.tags.slice(0, 4) as tag}
        <span class="chip">{tag}</span>
      {/each}
    </div>

    <div class="mt-5 flex items-center justify-between pt-4 border-t border-ink-faint-light dark:border-ink-faint-dark">
      <a
        href={`/portfolio/${project.slug}`}
        class="inline-flex items-center gap-1 text-xs font-medium text-ink-light dark:text-ink-dark hover:text-accent-600 dark:hover:text-accent-400 transition-colors"
      >
        Read more
        <ArrowUpRight class="h-3.5 w-3.5" />
      </a>

      <div class="flex items-center gap-2">
        {#if project.githubUrl}
          <a
            href={project.githubUrl}
            target="_blank"
            rel="noopener noreferrer"
            class="text-ink-muted-light dark:text-ink-muted-dark hover:text-ink-light dark:hover:text-ink-dark transition-colors"
            aria-label="GitHub repo"
          >
            <Github class="h-4 w-4" />
          </a>
        {/if}
        {#if project.demoUrl}
          <a
            href={project.demoUrl}
            target="_blank"
            rel="noopener noreferrer"
            class="text-ink-muted-light dark:text-ink-muted-dark hover:text-ink-light dark:hover:text-ink-dark transition-colors"
            aria-label="Live demo"
          >
            <ArrowUpRight class="h-4 w-4" />
          </a>
        {/if}
      </div>
    </div>
  </div>
</article>
