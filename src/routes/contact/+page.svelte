<script lang="ts">
  import {
    Mail,
    Linkedin,
    Github,
    Instagram,
    Send,
    CheckCircle,
    AlertCircle,
    ArrowUpRight,
  } from 'lucide-svelte';
  import { submitContact } from '$lib/api';

  let name = '';
  let email = '';
  let message = '';
  let isSubmitting = false;
  let submitStatus: 'idle' | 'success' | 'error' = 'idle';
  let errorMessage = '';

  const channels = [
    {
      label: 'Email',
      value: 'pradana@pradanayahya.com',
      href: 'mailto:pradana@pradanayahya.com',
      icon: Mail,
    },
    {
      label: 'LinkedIn',
      value: 'pradana-yahya',
      href: 'https://www.linkedin.com/in/pradana-yahya/',
      icon: Linkedin,
    },
    { label: 'GitHub', value: 'haipradana', href: 'https://github.com/haipradana', icon: Github },
    {
      label: 'Instagram',
      value: 'pradanaabdillah',
      href: 'https://instagram.com/pradanaabdillah',
      icon: Instagram,
    },
  ];

  async function handleSubmit(event: Event) {
    event.preventDefault();
    if (!name.trim() || !email.trim() || !message.trim()) return;

    isSubmitting = true;
    submitStatus = 'idle';

    try {
      await submitContact({ name, email, message });
      submitStatus = 'success';
      name = '';
      email = '';
      message = '';
      setTimeout(() => (submitStatus = 'idle'), 5000);
    } catch {
      submitStatus = 'error';
      errorMessage = 'Failed to send message. Please try again later.';
    } finally {
      isSubmitting = false;
    }
  }
</script>

<svelte:head>
  <title>Contact — Pradana Yahya</title>
  <meta name="description" content="Get in touch with Pradana Yahya Abdillah." />
</svelte:head>

<section class="mx-auto max-w-5xl px-5 sm:px-8 pt-14 lg:pt-20 pb-10">
  <p class="eyebrow">Contact</p>
  <h1 class="font-display text-4xl lg:text-5xl mt-3 text-ink-light dark:text-ink-dark text-balance">
    Say hello — I read everything.
  </h1>
  <p class="mt-4 max-w-2xl text-[15px] leading-relaxed text-ink-muted-light dark:text-ink-muted-dark">
    Whether it’s a collaboration, a research idea, or just a friendly note —
    reach out through any of these channels, or drop a message below.
  </p>
</section>

<section class="mx-auto max-w-5xl px-5 sm:px-8 pb-16 grid gap-10 lg:grid-cols-12">
  <!-- Channels -->
  <div class="lg:col-span-5 space-y-2">
    {#each channels as c}
      <a
        href={c.href}
        target={c.href.startsWith('http') ? '_blank' : undefined}
        rel="noopener noreferrer"
        class="group flex items-center justify-between gap-4 rounded-2xl border border-ink-faint-light dark:border-ink-faint-dark bg-surface-light-elev dark:bg-surface-dark-elev px-5 py-4 transition-all hover:border-accent-300 dark:hover:border-accent-700 hover:-translate-y-0.5"
      >
        <div class="flex items-center gap-3 min-w-0">
          <span class="inline-flex h-9 w-9 items-center justify-center rounded-lg bg-surface-light-muted dark:bg-surface-dark-muted text-ink-light dark:text-ink-dark">
            <svelte:component this={c.icon} class="h-4 w-4" />
          </span>
          <div class="min-w-0">
            <p class="text-[11px] uppercase tracking-[0.18em] text-ink-muted-light dark:text-ink-muted-dark">{c.label}</p>
            <p class="text-sm font-medium text-ink-light dark:text-ink-dark truncate">{c.value}</p>
          </div>
        </div>
        <ArrowUpRight class="h-4 w-4 text-ink-muted-light dark:text-ink-muted-dark group-hover:text-accent-600 dark:group-hover:text-accent-400 transition-colors" />
      </a>
    {/each}
  </div>

  <!-- Form -->
  <div class="lg:col-span-7">
    <form on:submit={handleSubmit} class="surface rounded-2xl p-6 sm:p-8 space-y-4">
      <h2 class="font-display text-xl text-ink-light dark:text-ink-dark">Send a message</h2>

      <div class="grid sm:grid-cols-2 gap-4">
        <div>
          <label for="name" class="block text-xs font-medium text-ink-muted-light dark:text-ink-muted-dark mb-1.5">Name</label>
          <input
            type="text"
            id="name"
            bind:value={name}
            required
            disabled={isSubmitting}
            placeholder="Your name"
            class="w-full px-3.5 py-2.5 rounded-lg bg-surface-light dark:bg-surface-dark border border-ink-faint-light dark:border-ink-faint-dark text-ink-light dark:text-ink-dark placeholder:text-ink-muted-light/60 dark:placeholder:text-ink-muted-dark/60 focus:border-accent-500 focus:outline-none transition-colors"
          />
        </div>
        <div>
          <label for="email" class="block text-xs font-medium text-ink-muted-light dark:text-ink-muted-dark mb-1.5">Email</label>
          <input
            type="email"
            id="email"
            bind:value={email}
            required
            disabled={isSubmitting}
            placeholder="you@example.com"
            class="w-full px-3.5 py-2.5 rounded-lg bg-surface-light dark:bg-surface-dark border border-ink-faint-light dark:border-ink-faint-dark text-ink-light dark:text-ink-dark placeholder:text-ink-muted-light/60 dark:placeholder:text-ink-muted-dark/60 focus:border-accent-500 focus:outline-none transition-colors"
          />
        </div>
      </div>

      <div>
        <label for="message" class="block text-xs font-medium text-ink-muted-light dark:text-ink-muted-dark mb-1.5">Message</label>
        <textarea
          id="message"
          bind:value={message}
          required
          disabled={isSubmitting}
          rows="5"
          placeholder="What’s on your mind?"
          class="w-full px-3.5 py-2.5 rounded-lg bg-surface-light dark:bg-surface-dark border border-ink-faint-light dark:border-ink-faint-dark text-ink-light dark:text-ink-dark placeholder:text-ink-muted-light/60 dark:placeholder:text-ink-muted-dark/60 focus:border-accent-500 focus:outline-none transition-colors resize-none"
        ></textarea>
      </div>

      <button
        type="submit"
        disabled={isSubmitting || !name.trim() || !email.trim() || !message.trim()}
        class="btn-primary w-full disabled:opacity-50 disabled:cursor-not-allowed"
      >
        {#if isSubmitting}
          <svg class="animate-spin h-4 w-4" viewBox="0 0 24 24" fill="none">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"></path>
          </svg>
          Sending…
        {:else}
          <Send class="h-4 w-4" /> Send message
        {/if}
      </button>

      {#if submitStatus === 'success'}
        <div class="flex items-start gap-2 p-3 rounded-lg bg-accent-50 dark:bg-accent-900/30 text-accent-700 dark:text-accent-200 text-sm">
          <CheckCircle class="h-4 w-4 mt-0.5 flex-shrink-0" />
          <p>Message sent — thank you for reaching out!</p>
        </div>
      {/if}

      {#if submitStatus === 'error'}
        <div class="flex items-start gap-2 p-3 rounded-lg bg-red-50 dark:bg-red-900/20 text-red-700 dark:text-red-300 text-sm">
          <AlertCircle class="h-4 w-4 mt-0.5 flex-shrink-0" />
          <p>{errorMessage}</p>
        </div>
      {/if}
    </form>
  </div>
</section>
