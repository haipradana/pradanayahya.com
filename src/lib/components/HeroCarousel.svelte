<script lang="ts">
  import { onMount, onDestroy } from 'svelte';
  import { ChevronLeft, ChevronRight, X } from 'lucide-svelte';

  export let images: { src: string; alt: string; caption?: string }[] = [];
  export let interval = 5500;

  let index = 0;
  let timer: ReturnType<typeof setInterval> | null = null;
  let paused = false;
  let lightboxOpen = false;

  // Touch gesture support
  let touchStartX = 0;
  let touchEndX = 0;

  function go(next: number) {
    if (!images.length) return;
    index = (next + images.length) % images.length;
  }

  function start() {
    stop();
    if (images.length < 2) return;
    timer = setInterval(() => {
      if (!paused && !lightboxOpen) go(index + 1);
    }, interval);
  }

  function stop() {
    if (timer) {
      clearInterval(timer);
      timer = null;
    }
  }

  function openLightbox(i?: number) {
    if (typeof i === 'number') index = i;
    lightboxOpen = true;
  }

  function closeLightbox() {
    lightboxOpen = false;
  }

  function handleKeydown(e: KeyboardEvent) {
    if (!lightboxOpen) return;
    if (e.key === 'ArrowLeft') {
      go(index - 1);
    } else if (e.key === 'ArrowRight') {
      go(index + 1);
    } else if (e.key === 'Escape') {
      closeLightbox();
    }
  }

  function handleTouchStart(e: TouchEvent) {
    touchStartX = e.changedTouches[0].screenX;
  }

  function handleTouchEnd(e: TouchEvent) {
    touchEndX = e.changedTouches[0].screenX;
    handleSwipe();
  }

  function handleSwipe() {
    const diff = touchStartX - touchEndX;
    if (Math.abs(diff) > 40) {
      if (diff > 0) {
        go(index + 1);
      } else {
        go(index - 1);
      }
    }
  }

  onMount(start);
  onDestroy(stop);
</script>

<svelte:window on:keydown={handleKeydown} />

<!-- Main Hero Carousel Card -->
<div
  class="group relative aspect-[4/3] w-full overflow-hidden rounded-[20px] border border-ink-faint-light dark:border-ink-faint-dark shadow-[0_30px_80px_-30px_rgba(0,0,0,0.25)] dark:shadow-[0_30px_80px_-20px_rgba(0,0,0,0.7)] bg-surface-light-muted dark:bg-surface-dark-muted select-none"
  on:mouseenter={() => (paused = true)}
  on:mouseleave={() => (paused = false)}
  on:focusin={() => (paused = true)}
  on:focusout={() => (paused = false)}
  on:touchstart={handleTouchStart}
  on:touchend={handleTouchEnd}
  role="region"
  aria-label="Photo carousel"
>
  {#each images as image, i}
    <div
      class="absolute inset-0 transition-opacity duration-[1000ms] ease-in-out cursor-pointer"
      style:opacity={i === index ? 1 : 0}
      style:z-index={i === index ? 1 : 0}
      aria-hidden={i !== index}
      on:click={() => openLightbox(i)}
      on:keydown={(e) => (e.key === 'Enter' || e.key === ' ') && openLightbox(i)}
      tabindex="0"
      role="button"
      aria-label={`View photo ${i + 1}: ${image.caption || image.alt}`}
    >
      <img
        src={image.src}
        alt={image.alt}
        class="h-full w-full object-cover transition-transform duration-700 group-hover:scale-105"
        loading={i === 0 ? 'eager' : 'lazy'}
        decoding="async"
      />
      <!-- Gradient overlay for text contrast -->
      <div
        class="absolute inset-x-0 bottom-0 h-40 bg-gradient-to-t from-black/85 via-black/35 to-transparent"
      />

      <!-- Caption (Positioned above dots) -->
      {#if image.caption}
        <div class="absolute bottom-8 left-4 right-4 text-[13.5px] sm:text-[14px] text-white/95 font-medium tracking-wide drop-shadow truncate">
          {image.caption}
        </div>
      {/if}
    </div>
  {/each}

  {#if images.length > 1}
    <!-- Controls (Side Navigation Arrows on hover/desktop) -->
    <button
      type="button"
      on:click|stopPropagation={() => go(index - 1)}
      class="absolute left-2.5 top-1/2 -translate-y-1/2 z-10 inline-flex h-9 w-9 items-center justify-center rounded-full bg-black/40 backdrop-blur-md text-white opacity-0 group-hover:opacity-100 hover:bg-black/70 hover:scale-110 transition-all duration-200"
      aria-label="Previous photo"
    >
      <ChevronLeft class="h-5 w-5" />
    </button>
    <button
      type="button"
      on:click|stopPropagation={() => go(index + 1)}
      class="absolute right-2.5 top-1/2 -translate-y-1/2 z-10 inline-flex h-9 w-9 items-center justify-center rounded-full bg-black/40 backdrop-blur-md text-white opacity-0 group-hover:opacity-100 hover:bg-black/70 hover:scale-110 transition-all duration-200"
      aria-label="Next photo"
    >
      <ChevronRight class="h-5 w-5" />
    </button>

    <!-- Indicators (Dots at bottom-3) -->
    <div class="absolute left-4 bottom-3 z-10 flex items-center gap-1.5 pointer-events-auto">
      {#each images as _, i}
        <button
          type="button"
          on:click|stopPropagation={() => go(i)}
          aria-label={`Go to slide ${i + 1}`}
          class="h-1.5 rounded-full transition-all duration-300 {i === index ? 'w-6 bg-white' : 'w-1.5 bg-white/40 hover:bg-white/75'}"
        ></button>
      {/each}
    </div>
  {/if}
</div>

<!-- Full-Screen Lightbox Modal -->
{#if lightboxOpen && images[index]}
  <div
    class="fixed inset-0 z-50 flex items-center justify-center bg-black/90 backdrop-blur-md p-4 sm:p-8 animate-fade-in select-none"
    on:click={closeLightbox}
    on:keydown={(e) => e.key === 'Escape' && closeLightbox()}
    role="dialog"
    aria-modal="true"
    aria-label="Photo Lightbox"
    tabindex="-1"
  >
    <!-- Close Button -->
    <button
      type="button"
      on:click={closeLightbox}
      class="absolute top-4 right-4 sm:top-6 sm:right-6 z-50 inline-flex h-11 w-11 items-center justify-center rounded-full bg-white/10 hover:bg-white/20 text-white backdrop-blur-md transition-colors"
      aria-label="Close lightbox"
    >
      <X class="h-6 w-6" />
    </button>

    <!-- Lightbox Main Image Container -->
    <div
      class="relative flex max-h-[85vh] max-w-[92vw] md:max-w-4xl flex-col items-center justify-center"
      on:click|stopPropagation
      on:touchstart={handleTouchStart}
      on:touchend={handleTouchEnd}
      role="document"
    >
      <img
        src={images[index].src}
        alt={images[index].alt}
        class="max-h-[75vh] w-auto max-w-full rounded-2xl object-contain shadow-2xl border border-white/10"
      />

      <!-- Caption & Counter Footer -->
      <div class="mt-4 flex items-center justify-between w-full max-w-xl px-2 text-white">
        <span class="text-sm font-medium tracking-wide text-white/90">
          {images[index].caption || images[index].alt}
        </span>
        <span class="text-xs font-mono text-white/60 bg-white/10 px-2.5 py-1 rounded-full backdrop-blur-sm">
          {index + 1} / {images.length}
        </span>
      </div>
    </div>

    <!-- Navigation Side Arrows in Lightbox -->
    {#if images.length > 1}
      <button
        type="button"
        on:click|stopPropagation={() => go(index - 1)}
        class="absolute left-3 sm:left-6 top-1/2 -translate-y-1/2 z-50 inline-flex h-12 w-12 items-center justify-center rounded-full bg-white/10 hover:bg-white/25 text-white backdrop-blur-md transition-all hover:scale-110"
        aria-label="Previous photo"
      >
        <ChevronLeft class="h-7 w-7" />
      </button>
      <button
        type="button"
        on:click|stopPropagation={() => go(index + 1)}
        class="absolute right-3 sm:right-6 top-1/2 -translate-y-1/2 z-50 inline-flex h-12 w-12 items-center justify-center rounded-full bg-white/10 hover:bg-white/25 text-white backdrop-blur-md transition-all hover:scale-110"
        aria-label="Next photo"
      >
        <ChevronRight class="h-7 w-7" />
      </button>
    {/if}
  </div>
{/if}

