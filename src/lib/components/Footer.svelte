<script lang="ts">
  import { Github, Linkedin, Mail, Twitter } from 'lucide-svelte';

  const year = new Date().getFullYear();

  const socials = [
    { href: 'https://github.com/haipradana', label: 'GitHub', icon: Github },
    { href: 'https://linkedin.com/in/pradana-yahya', label: 'LinkedIn', icon: Linkedin },
    { href: 'https://x.com/haipradana', label: 'Twitter / X', icon: Twitter },
    { href: 'mailto:pradana@pradanayahya.com', label: 'Email', icon: Mail },
  ];
</script>

<footer class="mt-24 border-t border-ink-faint-light dark:border-ink-faint-dark">
  <div class="mx-auto max-w-6xl px-5 sm:px-8 py-10">
    <div class="grid gap-8 md:grid-cols-12 md:items-end">
      <div class="md:col-span-7">
        <p class="font-display text-2xl text-ink-light dark:text-ink-dark">
          Let’s build something thoughtful.
        </p>
        <p class="mt-2 text-sm text-ink-muted-light dark:text-ink-muted-dark">
          Open to AI engineering, research, and collaboration opportunities.
        </p>
        <div class="mt-4 flex flex-wrap gap-2">
          <a href="/contact" class="btn-primary">Get in touch</a>
          <a
            href="mailto:pradana@pradanayahya.com"
            class="btn-ghost"
          >
            <Mail class="h-4 w-4" />
            pradana@pradanayahya.com
          </a>
        </div>
      </div>

      <div class="md:col-span-5 flex md:justify-end">
        <div class="flex items-center gap-1">
          {#each socials as s}
            <a
              href={s.href}
              target={s.href.startsWith('http') ? '_blank' : undefined}
              rel="noopener noreferrer"
              aria-label={s.label}
              class="inline-flex h-9 w-9 items-center justify-center rounded-full text-ink-muted-light dark:text-ink-muted-dark hover:bg-surface-light-muted dark:hover:bg-surface-dark-muted transition-colors"
            >
              <svelte:component this={s.icon} class="h-4 w-4" />
            </a>
          {/each}
        </div>
      </div>
    </div>

    <div class="mt-10 flex flex-col md:flex-row md:items-center md:justify-between gap-3 pt-6 border-t border-ink-faint-light dark:border-ink-faint-dark">
      <p class="text-xs text-ink-muted-light dark:text-ink-muted-dark">
        © {year} Pradana Yahya Abdillah.
      </p>
      <p class="text-xs text-ink-muted-light dark:text-ink-muted-dark">
        Yogyakarta, Indonesia
      </p>
    </div>
  </div>
</footer>
