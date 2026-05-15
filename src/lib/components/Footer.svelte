<script lang="ts">
  import { Github, Linkedin, Mail, Twitter } from 'lucide-svelte';
</script>

<footer class="border-t border-gray-200 dark:border-gray-800 mt-16">
  <div class="w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 xl:px-10 py-7">
    <div class="flex flex-col md:flex-row items-center justify-between gap-4">
      <p class="text-gray-600 dark:text-gray-400 text-sm mb-4 md:mb-0">
        2025-PRESENT © Pradana Yahya Abdillah
      </p>
      
      <div class="flex items-center gap-3">
        <a
          href="https://github.com/haipradana"
          target="_blank"
          rel="noopener noreferrer"
          class="p-1.5 text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-gray-100 transition-colors"
          aria-label="GitHub"
        >
          <Github class="w-4 h-4" />
        </a>
        <a
          href="https://linkedin.com/in/pradana-yahya"
          target="_blank"
          rel="noopener noreferrer"
          class="p-1.5 text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-gray-100 transition-colors"
          aria-label="LinkedIn"
        >
          <Linkedin class="w-4 h-4" />
        </a>
        <a
          href="https://x.com/haipradana"
          target="_blank"
          rel="noopener noreferrer"
          class="p-1.5 text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-gray-100 transition-colors"
          aria-label="Twitter"
        >
          <Twitter class="w-4 h-4" />
        </a>
        <a
          href="mailto:pradanayahyaabdillah@mail.ugm.ac.id"
          class="p-1.5 text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-gray-100 transition-colors"
          aria-label="Email"
        >
          <Mail class="w-4 h-4" />
        </a>
      </div>
    </div>
  </div>
</footer>
