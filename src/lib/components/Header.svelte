<script lang="ts">
  import { page } from '$app/stores';
  import { theme } from '$lib/stores/theme';
  import { Sun, Moon, Menu, X } from 'lucide-svelte';
  import { onMount } from 'svelte';
  import { fly } from 'svelte/transition';

  type NavItem = { href: string; label: string; match: (path: string) => boolean };

  const nav: NavItem[] = [
    { href: '/', label: 'About', match: (p) => p === '/' },
    { href: '/portfolio', label: 'Projects', match: (p) => p.startsWith('/portfolio') },
    { href: '/experience', label: 'Experience', match: (p) => p.startsWith('/experience') || p.startsWith('/honour') },
    { href: '/awards', label: 'Awards', match: (p) => p.startsWith('/awards') },
    { href: '/blogs', label: 'Writings', match: (p) => p.startsWith('/blogs') },
    { href: '/contact', label: 'Contact', match: (p) => p === '/contact' },
  ];

  let mobileOpen = false;
  let scrolled = false;

  onMount(() => {
    theme.init();
    const onScroll = () => (scrolled = window.scrollY > 24);
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
    return () => window.removeEventListener('scroll', onScroll);
  });

  $: currentPath = $page.url.pathname;
</script>

<header
  class="sticky top-0 z-50 transition-all duration-300"
  class:scrolled
>
  <div
    class="mx-auto transition-[max-width,padding] duration-300 ease-out"
    class:max-w-6xl={!scrolled}
    class:max-w-3xl={scrolled}
    class:px-5={!scrolled}
    class:sm:px-8={!scrolled}
    class:px-3={scrolled}
    class:sm:px-4={scrolled}
  >
    <div
      class="mt-3 flex items-center justify-between transition-all duration-300 ease-out"
      class:h-14={!scrolled}
      class:h-12={scrolled}
      class:rounded-full={scrolled}
      class:px-3={scrolled}
      class:sm:px-4={scrolled}
      class:pill={scrolled}
    >
      <a href="/" class="group flex items-center pl-1" aria-label="Home">
        <span class="font-display text-[20px] font-medium tracking-tight text-ink-light dark:text-ink-dark">
          Pradana
        </span>
      </a>

      <nav class="hidden md:flex items-center gap-1">
        {#each nav as item}
          {@const active = item.match(currentPath)}
          <a
            href={item.href}
            class="relative px-3 py-1.5 text-[13.5px] font-medium transition-colors {active ? 'text-ink-light dark:text-ink-dark' : 'text-ink-muted-light dark:text-ink-muted-dark hover:text-ink-light dark:hover:text-ink-dark'}"
          >
            {item.label}
            {#if active}
              <span class="absolute left-3 right-3 -bottom-0.5 h-px bg-accent-500"></span>
            {/if}
          </a>
        {/each}
      </nav>

      <div class="flex items-center gap-1.5">
        <button
          on:click={theme.toggle}
          class="inline-flex h-8 w-8 items-center justify-center rounded-full text-ink-muted-light dark:text-ink-muted-dark hover:bg-surface-light-muted dark:hover:bg-surface-dark-muted transition-colors"
          aria-label="Toggle theme"
        >
          {#if $theme === 'dark'}
            <Sun class="h-4 w-4" />
          {:else}
            <Moon class="h-4 w-4" />
          {/if}
        </button>

        <button
          class="md:hidden inline-flex h-8 w-8 items-center justify-center rounded-full text-ink-muted-light dark:text-ink-muted-dark hover:bg-surface-light-muted dark:hover:bg-surface-dark-muted transition-colors"
          on:click={() => (mobileOpen = !mobileOpen)}
          aria-label="Toggle menu"
        >
          {#if mobileOpen}
            <X class="h-4 w-4" />
          {:else}
            <Menu class="h-4 w-4" />
          {/if}
        </button>
      </div>
    </div>

    {#if mobileOpen}
      <nav transition:fly={{ y: -8, duration: 180 }} class="md:hidden pb-4 pt-2">
        <div class="surface rounded-2xl p-2">
          {#each nav as item}
            {@const active = item.match(currentPath)}
            <a
              href={item.href}
              on:click={() => (mobileOpen = false)}
              class="block rounded-xl px-4 py-3 text-sm font-medium transition-colors {active ? 'bg-surface-light-muted dark:bg-surface-dark-muted text-ink-light dark:text-ink-dark' : 'text-ink-muted-light dark:text-ink-muted-dark'}"
            >
              {item.label}
            </a>
          {/each}
        </div>
      </nav>
    {/if}
  </div>
</header>

<style>
  /* Floating rounded pill when scrolled. */
  .pill {
    background-color: color-mix(in oklab, theme('colors.surface.light') 78%, transparent);
    backdrop-filter: blur(18px) saturate(140%);
    -webkit-backdrop-filter: blur(18px) saturate(140%);
    border: 1px solid theme('colors.ink.faint-light');
    box-shadow:
      0 1px 0 rgba(255, 255, 255, 0.6) inset,
      0 10px 30px -10px rgba(0, 0, 0, 0.12);
  }
  :global(.dark) .pill {
    background-color: color-mix(in oklab, theme('colors.surface.dark') 70%, transparent);
    border-color: theme('colors.ink.faint-dark');
    box-shadow:
      0 1px 0 rgba(255, 255, 255, 0.04) inset,
      0 10px 30px -10px rgba(0, 0, 0, 0.6);
  }
</style>
