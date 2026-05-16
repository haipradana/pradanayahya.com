<script lang="ts">
  import { honours, type HonourItem } from '$lib/data/honours';
  import { Briefcase, GraduationCap, MapPin } from 'lucide-svelte';

  const items: HonourItem[] = honours
    .filter((h) => h.type === 'experience' || h.type === 'education')
    .reverse();
</script>

<svelte:head>
  <title>Experience — Pradana Yahya</title>
  <meta name="description" content="Professional experience and education of Pradana Yahya Abdillah." />
</svelte:head>

<section class="mx-auto max-w-5xl px-5 sm:px-8 pt-14 lg:pt-20 pb-10">
  <p class="eyebrow">Experience</p>
  <h1 class="font-display text-4xl lg:text-5xl mt-3 text-ink-light dark:text-ink-dark text-balance">
    Where I’ve worked, and what I’ve worked on.
  </h1>
  <p class="mt-4 max-w-2xl text-[15px] leading-relaxed text-ink-muted-light dark:text-ink-muted-dark">
    A chronological view of the roles I’ve held — from research and internships
    to leading robotics teams.
  </p>
</section>

<section class="mx-auto max-w-5xl px-5 sm:px-8 pb-24">
  <ol class="relative space-y-10 border-l border-ink-faint-light dark:border-ink-faint-dark pl-6 sm:pl-8">
    {#each items as item}
      <li class="relative">
        <span
          class="absolute -left-[33px] sm:-left-[41px] top-1.5 inline-flex h-7 w-7 items-center justify-center rounded-full bg-surface-light-elev dark:bg-surface-dark-elev border border-ink-faint-light dark:border-ink-faint-dark"
        >
          <svelte:component
            this={item.type === 'education' ? GraduationCap : Briefcase}
            class="h-3.5 w-3.5 text-ink-muted-light dark:text-ink-muted-dark"
          />
        </span>

        <article class="surface rounded-2xl p-6 hover:border-accent-300 dark:hover:border-accent-700 transition-colors">
          <div class="flex flex-wrap items-center gap-x-3 gap-y-1">
            <span class="chip-accent">
              {item.type === 'education' ? 'Education' : 'Experience'}
            </span>
            {#if item.period}
              <span class="text-[12px] text-ink-muted-light dark:text-ink-muted-dark">
                {item.period.from}{#if item.period.to && item.period.to !== item.period.from} — {item.period.to}{/if}
              </span>
            {/if}
            {#if item.location}
              <span class="inline-flex items-center gap-1 text-[12px] text-ink-muted-light dark:text-ink-muted-dark">
                <MapPin class="h-3 w-3" />
                {item.location}
              </span>
            {/if}
          </div>

          <h2 class="font-display text-xl lg:text-2xl mt-3 text-ink-light dark:text-ink-dark">
            {item.title}
          </h2>
          {#if item.org}
            <p class="mt-1 text-sm font-medium text-ink-light/80 dark:text-ink-dark/80">
              {item.org}
            </p>
          {/if}
          {#if item.description}
            <p class="mt-3 text-[15px] leading-relaxed text-ink-muted-light dark:text-ink-muted-dark text-pretty">
              {item.description}
            </p>
          {/if}

          {#if item.tags?.length}
            <div class="mt-4 flex flex-wrap gap-1.5">
              {#each item.tags as t}
                <span class="chip">{t}</span>
              {/each}
            </div>
          {/if}
        </article>
      </li>
    {/each}
  </ol>
</section>
