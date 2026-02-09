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
        class="fixed bottom-24 right-6 z-40 w-12 h-12 rounded-full bg-gray-700 dark:bg-gray-600 text-white shadow-lg hover:shadow-xl transition-all duration-300 hover:scale-105 hover:bg-gray-600 dark:hover:bg-gray-500 flex items-center justify-center"
        aria-label="Back to top"
    >
        <ArrowUp class="w-5 h-5" />
    </button>
{/if}
