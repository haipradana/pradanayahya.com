<script lang="ts">
  import '../app.css';
  import Header from '$lib/components/Header.svelte';
  import Footer from '$lib/components/Footer.svelte';
  import ChatWidget from '$lib/components/ChatWidget.svelte';
  import { page } from '$app/stores';
  
  // Don't show chat widget on admin pages
  $: isAdminPage = $page.url.pathname.startsWith('/admin');
</script>

<div class="min-h-screen flex flex-col">
  <Header />
  
  <main class="flex-1">
    <slot />
  </main>
  
  <Footer />
</div>

<!-- Chat Widget (hidden on admin pages) -->
{#if !isAdminPage}
  <ChatWidget />
{/if}