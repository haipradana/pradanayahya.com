<script lang="ts">
  import '../app.css';
  import Header from '$lib/components/Header.svelte';
  import Footer from '$lib/components/Footer.svelte';
  import ChatWidget from '$lib/components/ChatWidget.svelte';
  import BackToTop from '$lib/components/BackToTop.svelte';
  import { page } from '$app/stores';

  const SITE = 'https://pradanayahya.com';

  // Pathnames where we hide the public chrome / chat / back-to-top.
  $: isAdminPage = $page.url.pathname.startsWith('/admin');

  // Canonical without trailing slash (except root) so duplicates collapse.
  $: pathname = $page.url.pathname;
  $: canonical = pathname === '/'
    ? `${SITE}/`
    : `${SITE}${pathname.replace(/\/$/, '')}`;
</script>

<svelte:head>
  <link rel="canonical" href={canonical} />
  <link rel="alternate" hreflang="en" href={canonical} />
  <link rel="alternate" hreflang="id" href={canonical} />
  <meta property="og:url" content={canonical} />
  <meta name="twitter:url" content={canonical} />
</svelte:head>

<div class="min-h-screen flex flex-col">
  <Header />

  <main class="flex-1">
    <slot />
  </main>

  <Footer />
</div>

{#if !isAdminPage}
  <BackToTop />
  <ChatWidget />
{/if}
