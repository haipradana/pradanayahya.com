<script lang="ts">
    import { onMount } from "svelte";
    import { ArrowUp } from "lucide-svelte";
    import { fade } from "svelte/transition";

    let showButton = false;

    onMount(() => {
        const handleScroll = () => {
            showButton = window.scrollY > 300;
        };

        window.addEventListener("scroll", handleScroll);

        return () => {
            window.removeEventListener("scroll", handleScroll);
        };
    });

    function scrollToTop() {
        window.scrollTo({
            top: 0,
            behavior: "smooth",
        });
    }
</script>

{#if showButton}
    <button
        on:click={scrollToTop}
        transition:fade={{ duration: 200 }}
        class="fixed bottom-24 right-6 z-40 w-10 h-10 rounded-full bg-surface-light-elev dark:bg-surface-dark-elev text-ink-light dark:text-ink-dark border border-ink-faint-light dark:border-ink-faint-dark shadow-lg hover:shadow-xl transition-all duration-300 hover:-translate-y-0.5 flex items-center justify-center"
        aria-label="Back to top"
    >
        <ArrowUp class="w-4 h-4" />
    </button>
{/if}
