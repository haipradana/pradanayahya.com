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

<header class="sticky top-0 z-50">
  <div class="nav-outer mx-auto" class:is-scrolled={scrolled}>
    <div class="nav-pill mt-3 flex items-center justify-between" class:is-scrolled={scrolled}>
      <a href="/" class="group flex items-center pl-1" aria-label="Home">
        <span class="font-display text-[22px] font-medium tracking-tight text-ink-light dark:text-ink-dark">
          Pradana
        </span>
      </a>

      <nav class="hidden md:flex items-center gap-1">
        {#each nav as item}
          {@const active = item.match(currentPath)}
          <a
            href={item.href}
            class="relative px-3 py-2 text-[14px] font-medium transition-colors {active ? 'text-ink-light dark:text-ink-dark' : 'text-ink-muted-light dark:text-ink-muted-dark hover:text-ink-light dark:hover:text-ink-dark'}"
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
          class="inline-flex h-10 w-10 items-center justify-center rounded-full text-ink-muted-light dark:text-ink-muted-dark hover:bg-surface-light-muted dark:hover:bg-surface-dark-muted transition-colors"
          aria-label="Toggle theme"
        >
          {#if $theme === 'dark'}
            <Sun class="h-[18px] w-[18px]" />
          {:else}
            <Moon class="h-[18px] w-[18px]" />
          {/if}
        </button>

        <button
          class="md:hidden inline-flex h-10 w-10 items-center justify-center rounded-full text-ink-muted-light dark:text-ink-muted-dark hover:bg-surface-light-muted dark:hover:bg-surface-dark-muted transition-colors"
          on:click={() => (mobileOpen = !mobileOpen)}
          aria-label="Toggle menu"
        >
          {#if mobileOpen}
            <X class="h-[18px] w-[18px]" />
          {:else}
            <Menu class="h-[18px] w-[18px]" />
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
  /* ── Outer wrapper: max-width + horizontal padding ──────────────── */
  .nav-outer {
    max-width: 72rem; /* max-w-6xl */
    padding-left: 1.25rem;   /* px-5 */
    padding-right: 1.25rem;
    transition:
      max-width 300ms ease-out,
      padding-left 300ms ease-out,
      padding-right 300ms ease-out;
  }
  @media (min-width: 640px) {
    .nav-outer { padding-left: 2rem; padding-right: 2rem; } /* sm:px-8 */
    .nav-outer.is-scrolled { padding-left: 1rem; padding-right: 1rem; }
  }
  .nav-outer.is-scrolled {
    max-width: 48rem; /* max-w-3xl */
    padding-left: 0.75rem;
    padding-right: 0.75rem;
  }

  /* ── Inner pill: height, radius, bg, border, shadow, blur ───────── */
  .nav-pill {
    height: 4rem;              /* h-16 */
    border-radius: 0;
    padding-left: 0;
    padding-right: 0;
    background-color: transparent;
    backdrop-filter: blur(0px);
    -webkit-backdrop-filter: blur(0px);
    border: 1px solid transparent;
    box-shadow: none;
    transition:
      height 300ms ease-out,
      border-radius 300ms ease-out,
      padding-left 300ms ease-out,
      padding-right 300ms ease-out,
      background-color 300ms ease-out,
      backdrop-filter 300ms ease-out,
      -webkit-backdrop-filter 300ms ease-out,
      border-color 300ms ease-out,
      box-shadow 300ms ease-out;
  }
  .nav-pill.is-scrolled {
    height: 3.5rem;            /* h-14 */
    border-radius: 9999px;
    padding-left: 1rem;        /* px-4 */
    padding-right: 1rem;
    background-color: color-mix(in oklab, theme('colors.surface.light') 78%, transparent);
    backdrop-filter: blur(18px) saturate(140%);
    -webkit-backdrop-filter: blur(18px) saturate(140%);
    border-color: theme('colors.ink.faint-light');
    box-shadow:
      0 1px 0 rgba(255, 255, 255, 0.6) inset,
      0 10px 30px -10px rgba(0, 0, 0, 0.12);
  }
  @media (min-width: 640px) {
    .nav-pill.is-scrolled { padding-left: 1.25rem; padding-right: 1.25rem; }
  }
  :global(.dark) .nav-pill.is-scrolled {
    background-color: color-mix(in oklab, theme('colors.surface.dark') 70%, transparent);
    border-color: theme('colors.ink.faint-dark');
    box-shadow:
      0 1px 0 rgba(255, 255, 255, 0.04) inset,
      0 10px 30px -10px rgba(0, 0, 0, 0.6);
  }
</style>
