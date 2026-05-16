<script lang="ts">
  import {
    blogPosts,
    groupPostsByYear,
    formatDate,
  } from '$lib/data/blogPosts';
  import { ArrowUpRight } from 'lucide-svelte';

  $: postsByYear = groupPostsByYear(blogPosts);
  $: years = [...postsByYear.keys()].sort((a, b) => b - a);
</script>

<svelte:head>
  <title>Writings — Pradana Yahya</title>
  <meta
    name="description"
    content="Notes and essays on machine learning, AI engineering, and the craft of building things."
  />
</svelte:head>

<section class="mx-auto max-w-3xl px-5 sm:px-8 pt-14 lg:pt-20 pb-10">
  <p class="eyebrow">Writings</p>
  <h1 class="font-display text-4xl lg:text-5xl mt-3 text-ink-light dark:text-ink-dark text-balance">
    Notes from the workbench.
  </h1>
  <p class="mt-4 max-w-xl text-[15px] leading-relaxed text-ink-muted-light dark:text-ink-muted-dark">
    Occasional essays on machine learning, AI engineering, and lessons from
    building things.
  </p>
</section>

<section class="mx-auto max-w-3xl px-5 sm:px-8 pb-24">
  {#each years as year}
    <div class="mb-14">
      <div class="flex items-baseline justify-between border-b border-ink-faint-light dark:border-ink-faint-dark pb-3 mb-6">
        <h2 class="font-display text-xl text-ink-light dark:text-ink-dark">{year}</h2>
        <span class="text-[11px] uppercase tracking-[0.18em] text-ink-muted-light dark:text-ink-muted-dark">
          {postsByYear.get(year)?.length ?? 0} {(postsByYear.get(year)?.length ?? 0) === 1 ? 'post' : 'posts'}
        </span>
      </div>

      <ul class="divide-y divide-ink-faint-light dark:divide-ink-faint-dark">
        {#each postsByYear.get(year) ?? [] as post}
          <li>
            <a
              href={`/blogs/${post.slug}`}
              class="group grid grid-cols-12 gap-4 py-5 items-baseline"
            >
              <div class="col-span-12 sm:col-span-2 text-[12px] text-ink-muted-light dark:text-ink-muted-dark">
                {formatDate(post.date)}
              </div>
              <div class="col-span-12 sm:col-span-8">
                <h3 class="font-display text-lg leading-snug text-ink-light dark:text-ink-dark group-hover:text-accent-600 dark:group-hover:text-accent-400 transition-colors text-pretty">
                  {post.title}
                </h3>
              </div>
              <div class="col-span-12 sm:col-span-2 sm:text-right flex sm:justify-end items-center gap-1.5">
                <span class="chip">{post.category}</span>
                <ArrowUpRight class="h-3.5 w-3.5 text-ink-muted-light dark:text-ink-muted-dark opacity-0 group-hover:opacity-100 transition-opacity" />
              </div>
            </a>
          </li>
        {/each}
      </ul>
    </div>
  {/each}

  {#if years.length === 0}
    <div class="surface rounded-2xl py-20 text-center">
      <p class="text-ink-muted-light dark:text-ink-muted-dark">No posts yet. Check back soon.</p>
    </div>
  {/if}
</section>
