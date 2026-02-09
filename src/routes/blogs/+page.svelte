<script lang="ts">
    import {
        blogPosts,
        groupPostsByYear,
        formatDate,
    } from "$lib/data/blogPosts";

    $: postsByYear = groupPostsByYear(blogPosts);
    $: years = [...postsByYear.keys()].sort((a, b) => b - a);
</script>

<svelte:head>
    <title>Blog - Pradana Yahya</title>
    <meta
        name="description"
        content="Read my thoughts, learnings, and experiences in machine learning, data science, and technology."
    />
</svelte:head>

<div
    class="min-h-screen bg-white dark:bg-dark-custom py-16 lg:py-24 transition-colors duration-300"
>
    <div class="max-w-3xl mx-auto px-6 lg:px-8">
        {#each years as year}
            <section class="mb-12">
                <h2
                    class="text-xl font-semibold text-gray-800 dark:text-gray-200 mb-6 pb-2 border-b border-gray-200 dark:border-gray-700"
                >
                    {year}
                </h2>

                <div class="space-y-8">
                    {#each postsByYear.get(year) || [] as post}
                        <a href="/blogs/{post.slug}" class="group block">
                            <h3
                                class="text-lg lg:text-xl font-medium text-gray-900 dark:text-gray-100 group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors mb-1"
                            >
                                {post.title}
                            </h3>
                            <div
                                class="flex items-center text-sm text-gray-500 dark:text-gray-400"
                            >
                                <span>{formatDate(post.date)}</span>
                                <span class="mx-2">—</span>
                                <span class="text-blue-600 dark:text-blue-400"
                                    >{post.category}</span
                                >
                            </div>
                        </a>
                    {/each}
                </div>
            </section>
        {/each}

        {#if years.length === 0}
            <div class="text-center text-gray-500 dark:text-gray-400 py-20">
                <p class="text-lg">No posts yet. Check back soon!</p>
            </div>
        {/if}
    </div>
</div>
