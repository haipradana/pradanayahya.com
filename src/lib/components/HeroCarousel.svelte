<script lang="ts">
  import { onMount, onDestroy } from 'svelte';
  import { ChevronLeft, ChevronRight } from 'lucide-svelte';

  export let images: { src: string; alt: string; caption?: string }[] = [];
  export let interval = 5500;

  let index = 0;
  let timer: ReturnType<typeof setInterval> | null = null;
  let paused = false;

  function go(next: number) {
    if (!images.length) return;
    index = (next + images.length) % images.length;
  }

  function start() {
    stop();
    if (images.length < 2) return;
    timer = setInterval(() => {
      if (!paused) go(index + 1);
    }, interval);
  }

  function stop() {
    if (timer) {
      clearInterval(timer);
      timer = null;
    }
  }

  onMount(start);
  onDestroy(stop);
</script>

<div
  class="relative aspect-[5/4] w-full overflow-hidden rounded-[20px] border border-ink-faint-light dark:border-ink-faint-dark shadow-[0_30px_80px_-30px_rgba(0,0,0,0.25)] dark:shadow-[0_30px_80px_-20px_rgba(0,0,0,0.7)] bg-surface-light-muted dark:bg-surface-dark-muted"
  on:mouseenter={() => (paused = true)}
  on:mouseleave={() => (paused = false)}
  on:focusin={() => (paused = true)}
  on:focusout={() => (paused = false)}
  role="region"
  aria-label="Photo carousel"
>
  {#each images as image, i}
    <div
      class="absolute inset-0 transition-opacity duration-[1200ms] ease-out"
      style:opacity={i === index ? 1 : 0}
      style:z-index={i === index ? 1 : 0}
      aria-hidden={i !== index}
    >
      <img
        src={image.src}
        alt={image.alt}
        class="h-full w-full object-cover"
        loading={i === 0 ? 'eager' : 'lazy'}
        decoding="async"
      />
      <div
        class="absolute inset-x-0 bottom-0 h-32 bg-gradient-to-t from-black/60 via-black/10 to-transparent"
      />
      {#if image.caption}
        <div class="absolute bottom-4 left-5 right-16 text-[12px] text-white/90 font-medium tracking-wide drop-shadow">
          {image.caption}
        </div>
      {/if}
    </div>
  {/each}

  {#if images.length > 1}
    <!-- Controls -->
    <div class="absolute right-3 bottom-3 z-10 flex items-center gap-1.5">
      <button
        type="button"
        on:click={() => go(index - 1)}
        class="inline-flex h-9 w-9 items-center justify-center rounded-full bg-white/15 backdrop-blur-md text-white hover:bg-white/25 transition-colors"
        aria-label="Previous photo"
      >
        <ChevronLeft class="h-4 w-4" />
      </button>
      <button
        type="button"
        on:click={() => go(index + 1)}
        class="inline-flex h-9 w-9 items-center justify-center rounded-full bg-white/15 backdrop-blur-md text-white hover:bg-white/25 transition-colors"
        aria-label="Next photo"
      >
        <ChevronRight class="h-4 w-4" />
      </button>
    </div>

    <!-- Indicators -->
    <div class="absolute left-4 bottom-4 z-10 flex items-center gap-1.5">
      {#each images as _, i}
        <button
          type="button"
          on:click={() => go(i)}
          aria-label={`Go to slide ${i + 1}`}
          class="h-1.5 rounded-full transition-all duration-300 {i === index ? 'w-6 bg-white' : 'w-1.5 bg-white/50 hover:bg-white/75'}"
        ></button>
      {/each}
    </div>
  {/if}
</div>
