<script lang="ts">
  import { page } from '$app/stores';
  import { theme } from '$lib/stores/theme';
  import { Sun, Moon, Menu, X } from 'lucide-svelte';
  import { onMount } from 'svelte';

  let isMobileMenuOpen = false;

  onMount(() => {
    theme.init();
  });

  const toggleMobileMenu = () => {
    isMobileMenuOpen = !isMobileMenuOpen;
  };

  const closeMobileMenu = () => {
    isMobileMenuOpen = false;
  };

  $: currentPath = $page.url.pathname;
</script>

<header class="sticky top-0 z-50 bg-white/80 dark:bg-dark-custom/80 backdrop-blur-md border-b border-gray-200 dark:border-gray-700 transition-colors duration-300">
  <div class="max-w-3xl lg:max-w-4xl mx-auto px-6 lg:px-8">
          <div class="flex items-center justify-between h-12 lg:h-14">
      <!-- Logo -->
      <a href="/" class="py-1 sm:py-2 lg:py-3">
        {#if $theme === 'dark'}
          <img src="/images/logodana-dark.png" alt="Pradana Logo" class="h-8 sm:h-7 lg:h-8 w-auto" />
        {:else}
          <img src="/images/logodana-light.png" alt="Pradana Logo" class="h-8 sm:h-7 lg:h-8 w-auto" />
        {/if}
      </a>      

      <!-- Desktop Navigation -->
      <nav class="hidden md:flex items-center space-x-8 lg:space-x-10 xl:space-x-12">
        <a 
          href="/" 
          class="text-sm lg:text-base text-gray-700 dark:text-gray-300 hover:text-gray-900 dark:hover:text-gray-100 transition-colors {currentPath === '/' ? 'text-gray-900 dark:text-gray-100 font-medium' : ''}"
        >
          About
        </a>
        <a 
          href="/portfolio" 
          class="text-sm lg:text-base text-gray-700 dark:text-gray-300 hover:text-gray-900 dark:hover:text-gray-100 transition-colors {currentPath.startsWith('/portfolio') ? 'text-gray-900 dark:text-gray-100 font-medium' : ''}"
        >
          Projects
        </a>
        <a 
          href="/honour" 
          class="text-sm lg:text-base text-gray-700 dark:text-gray-300 hover:text-gray-900 dark:hover:text-gray-100 transition-colors {currentPath.startsWith('/honour') ? 'text-gray-900 dark:text-gray-100 font-medium' : ''}"
        >
          Experience
        </a>
        <a 
          href="/contact" 
          class="text-sm lg:text-base text-gray-700 dark:text-gray-300 hover:text-gray-900 dark:hover:text-gray-100 transition-colors {currentPath === '/contact' ? 'text-gray-900 dark:text-gray-100 font-medium' : ''}"
        >
          Reach me!
        </a>
      </nav>

      <!-- Theme Toggle & Mobile Menu Button -->
      <div class="flex items-center space-x-3 lg:space-x-4">
        <button
          on:click={theme.toggle}
          class="p-2 lg:p-3 xl:p-4 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors"
          aria-label="Toggle theme"
        >
          {#if $theme === 'dark'}
            <Sun class="w-5 h-5 lg:w-6 lg:h-6 xl:w-7 xl:h-7" />
          {:else}
            <Moon class="w-5 h-5 lg:w-6 lg:h-6 xl:w-7 xl:h-7" />
          {/if}
        </button>

        <!-- Mobile menu button -->
        <button
          class="md:hidden p-2 lg:p-3 xl:p-4 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors"
          on:click={toggleMobileMenu}
          aria-label="Toggle mobile menu"
        >
          {#if isMobileMenuOpen}
            <X class="w-5 h-5 lg:w-6 lg:h-6 xl:w-7 xl:h-7" />
          {:else}
            <Menu class="w-5 h-5 lg:w-6 lg:h-6 xl:w-7 xl:h-7" />
          {/if}
        </button>
      </div>
    </div>

    <!-- Mobile Navigation -->
    {#if isMobileMenuOpen}
      <nav class="md:hidden py-4 border-t border-gray-200 dark:border-gray-800">
        <div class="flex flex-col space-y-2">
          <a 
            href="/" 
            class="px-4 py-3 text-base text-gray-700 dark:text-gray-300 hover:text-gray-900 dark:hover:text-gray-100 transition-colors {currentPath === '/' ? 'text-gray-900 dark:text-gray-100 font-medium' : ''}"
            on:click={closeMobileMenu}
          >
            About
          </a>
          <a 
            href="/portfolio" 
            class="px-4 py-3 text-base text-gray-700 dark:text-gray-300 hover:text-gray-900 dark:hover:text-gray-100 transition-colors {currentPath.startsWith('/portfolio') ? 'text-gray-900 dark:text-gray-100 font-medium' : ''}"
            on:click={closeMobileMenu}
          >
            Projects
          </a>
          <a 
            href="/honour" 
            class="px-4 py-3 text-base text-gray-700 dark:text-gray-300 hover:text-gray-900 dark:hover:text-gray-100 transition-colors {currentPath.startsWith('/honour') ? 'text-gray-900 dark:text-gray-100 font-medium' : ''}"
            on:click={closeMobileMenu}
          >
            Honour
          </a>
          <a 
            href="/contact" 
            class="px-4 py-3 text-base text-gray-700 dark:text-gray-300 hover:text-gray-900 dark:hover:text-gray-100 transition-colors {currentPath === '/contact' ? 'text-gray-900 dark:text-gray-100 font-medium' : ''}"
            on:click={closeMobileMenu}
          >
            Reach me!
          </a>
        </div>
      </nav>
    {/if}
  </div>
</header>