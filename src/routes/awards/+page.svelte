<script lang="ts">
  import { honours, sortAwardsByBest, type HonourItem } from '$lib/data/honours';
  import { Trophy, MapPin } from 'lucide-svelte';

  const items: HonourItem[] = sortAwardsByBest(honours.filter((h) => h.type === 'award'));
</script>

<svelte:head>
  <title>Awards - Pradana Yahya</title>
  <meta name="description" content="Awards and competition results for Pradana Yahya Abdillah." />
</svelte:head>

<section class="mx-auto max-w-5xl px-5 sm:px-8 pt-14 lg:pt-20 pb-10">
  <p class="eyebrow">Awards</p>
  <h1 class="font-display text-4xl lg:text-5xl mt-3 text-ink-light dark:text-ink-dark text-balance">
    Competitions, podiums, and proud moments.
  </h1>
  <p class="mt-4 max-w-2xl text-[15px] leading-relaxed text-ink-muted-light dark:text-ink-muted-dark">
    Selected results from data science and machine learning competitions.
  </p>
</section>

<section class="mx-auto max-w-5xl px-5 sm:px-8 pb-24">
  <div class="grid gap-5 md:grid-cols-2">
    {#each items as item}
      <article class="surface rounded-2xl p-6 relative overflow-hidden group">
        <div class="absolute top-5 right-5 text-ink-faint-light dark:text-ink-faint-dark group-hover:text-accent-400 transition-colors">
          <Trophy class="h-8 w-8" />
        </div>
        <div class="flex flex-wrap items-center gap-x-3 gap-y-1">
          {#if item.period}
            <span class="chip-accent">{item.period.from}</span>
          {/if}
          {#if item.location}
            <span class="inline-flex items-center gap-1 text-[12px] text-ink-muted-light dark:text-ink-muted-dark">
              <MapPin class="h-3 w-3" />
              {item.location}
            </span>
          {/if}
        </div>

        <h2 class="font-display text-xl lg:text-2xl mt-3 pr-12 text-ink-light dark:text-ink-dark leading-tight">
          {item.title}
        </h2>
        {#if item.org}
          <p class="mt-1 text-sm font-medium text-ink-light/80 dark:text-ink-dark/80">
            {item.org}
          </p>
        {/if}
        {#if item.description}
          <p class="mt-3 text-[14.5px] leading-relaxed text-ink-muted-light dark:text-ink-muted-dark text-pretty">
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
    {/each}
  </div>
</section>
