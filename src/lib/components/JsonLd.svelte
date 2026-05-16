<script lang="ts">
  export let data: Record<string, unknown> | unknown[];

  const OPEN = '<' + 'script type="application/ld+json">';
  const CLOSE = '<' + '/script>';

  $: json = JSON.stringify(data).replace(/</g, '\\u003c');
  $: html = OPEN + json + CLOSE;
</script>

<svelte:head>
  {@html html}
</svelte:head>
