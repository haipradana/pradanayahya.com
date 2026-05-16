<script lang="ts">
    import { page } from "$app/stores";
    import { blogPosts, formatDate } from "$lib/data/blogPosts";
    import { marked } from "marked";
    import DOMPurify from "dompurify";
    import { onMount } from "svelte";
    import JsonLd from "$lib/components/JsonLd.svelte";

    $: slug = $page.params.slug;
    $: post = blogPosts.find((p) => p.slug === slug);

    // Parse markdown content
    $: htmlContent = post
        ? DOMPurify.sanitize(marked.parse(post.content) as string)
        : "";

    // Extract headings for table of contents
    interface TocItem {
        id: string;
        text: string;
        level: number;
    }

    let tocItems: TocItem[] = [];

    onMount(() => {
        if (post) {
            // Extract headings from markdown
            const headingRegex = /^(#{2,3})\s+(.+)$/gm;
            const matches = [...post.content.matchAll(headingRegex)];

            tocItems = matches.map((match) => ({
                id: match[2]
                    .toLowerCase()
                    .replace(/[^a-z0-9]+/g, "-")
                    .replace(/(^-|-$)/g, ""),
                text: match[2],
                level: match[1].length,
            }));
        }
    });

    function scrollToSection(id: string) {
        const element = document.getElementById(id);
        if (element) {
            element.scrollIntoView({ behavior: "smooth" });
        }
    }

    $: postDescription = post
        ? post.content.replace(/[#*`>_]/g, "").slice(0, 160).trim()
        : "";
    $: postJsonLd = post
        ? {
              "@context": "https://schema.org",
              "@type": "BlogPosting",
              headline: post.title,
              datePublished: post.date,
              dateModified: post.date,
              articleSection: post.category,
              url: "https://pradanayahya.com/blogs/" + post.slug,
              author: {
                  "@type": "Person",
                  name: "Pradana Yahya Abdillah",
                  url: "https://pradanayahya.com",
              },
              publisher: {
                  "@type": "Person",
                  name: "Pradana Yahya Abdillah",
              },
              mainEntityOfPage: {
                  "@type": "WebPage",
                  "@id": "https://pradanayahya.com/blogs/" + post.slug,
              },
          }
        : null;
</script>

<svelte:head>
    {#if post}
        <title>{post.title} — Pradana Yahya</title>
        <meta name="description" content={postDescription} />
        <meta property="og:type" content="article" />
        <meta property="og:title" content={`${post.title} — Pradana Yahya`} />
        <meta property="og:description" content={postDescription} />
        <meta property="article:published_time" content={post.date} />
        <meta property="article:author" content="Pradana Yahya Abdillah" />
        <meta property="article:section" content={post.category} />
    {:else}
        <title>Post Not Found — Pradana Yahya</title>
        <meta name="robots" content="noindex, follow" />
    {/if}
</svelte:head>

{#if postJsonLd}
    <JsonLd data={postJsonLd} />
{/if}

{#if post}
    <div
        class="min-h-screen bg-white dark:bg-dark-custom py-16 lg:py-24 transition-colors duration-300"
    >
        <div class="max-w-5xl mx-auto px-6 lg:px-8">
            <div class="lg:flex lg:gap-16">
                <!-- Main Content -->
                <article class="flex-1 max-w-3xl">
                    <header class="mb-10">
                        <h1
                            class="text-3xl lg:text-4xl font-bold text-gray-900 dark:text-white mb-3"
                        >
                            {post.title}
                        </h1>
                        <div
                            class="flex items-center text-sm text-gray-500 dark:text-gray-400"
                        >
                            <time>{formatDate(post.date)}</time>
                            <span class="mx-2">—</span>
                            <span class="text-blue-600 dark:text-blue-400"
                                >{post.category}</span
                            >
                        </div>
                    </header>

                    <div
                        class="prose prose-gray dark:prose-invert max-w-none blog-content"
                    >
                        {@html htmlContent}
                    </div>

                    <div
                        class="mt-16 pt-8 border-t border-gray-200 dark:border-gray-700"
                    >
                        <a
                            href="/blogs"
                            class="text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white transition-colors"
                        >
                            ← Back to all posts
                        </a>
                    </div>
                </article>

                <!-- Table of Contents Sidebar -->
                {#if tocItems.length > 0}
                    <aside class="hidden lg:block w-64 flex-shrink-0">
                        <div class="sticky top-24">
                            <h4
                                class="text-sm font-medium text-gray-500 dark:text-gray-400 mb-4"
                            >
                                On this page
                            </h4>
                            <nav class="space-y-2">
                                {#each tocItems as item}
                                    <button
                                        on:click={() =>
                                            scrollToSection(item.id)}
                                        class="block text-left text-sm text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white transition-colors {item.level ===
                                        3
                                            ? 'pl-4'
                                            : ''}"
                                    >
                                        {item.text}
                                    </button>
                                {/each}
                            </nav>
                        </div>
                    </aside>
                {/if}
            </div>
        </div>
    </div>
{:else}
    <div
        class="min-h-screen bg-white dark:bg-dark-custom flex items-center justify-center transition-colors duration-300"
    >
        <div class="text-center">
            <h1 class="text-2xl font-bold text-gray-900 dark:text-white mb-4">
                Post Not Found
            </h1>
            <a
                href="/blogs"
                class="text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white transition-colors"
            >
                ← Back to all posts
            </a>
        </div>
    </div>
{/if}

<style>
    :global(.blog-content h2) {
        font-size: 1.5rem;
        font-weight: 700;
        margin-top: 2.5rem;
        margin-bottom: 1rem;
    }

    :global(.blog-content h3) {
        font-size: 1.25rem;
        font-weight: 600;
        margin-top: 2rem;
        margin-bottom: 0.75rem;
    }

    :global(.blog-content p) {
        line-height: 1.75;
        margin-bottom: 1rem;
    }

    :global(.blog-content ul) {
        list-style-type: disc;
        list-style-position: inside;
        margin-bottom: 1rem;
    }

    :global(.blog-content ul li) {
        margin-bottom: 0.5rem;
    }

    :global(.blog-content ol) {
        list-style-type: decimal;
        list-style-position: inside;
        margin-bottom: 1rem;
    }

    :global(.blog-content ol li) {
        margin-bottom: 0.5rem;
    }

    :global(.blog-content a) {
        color: #2563eb;
        text-decoration: underline;
    }

    :global(.dark .blog-content a) {
        color: #60a5fa;
    }

    :global(.blog-content strong) {
        font-weight: 600;
    }

    :global(.blog-content code) {
        background-color: #f3f4f6;
        padding: 0.125rem 0.375rem;
        border-radius: 0.25rem;
        font-size: 0.875rem;
    }

    :global(.dark .blog-content code) {
        background-color: #1f2937;
        color: #e5e7eb;
    }

    :global(.blog-content pre) {
        background-color: #1f2937;
        padding: 1rem;
        border-radius: 0.5rem;
        overflow-x: auto;
        margin-bottom: 1rem;
    }

    :global(.blog-content pre code) {
        background-color: transparent;
        padding: 0;
        color: #e5e7eb;
    }

    :global(.blog-content blockquote) {
        border-left: 4px solid #d1d5db;
        padding-left: 1rem;
        font-style: italic;
        color: #6b7280;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }

    :global(.dark .blog-content blockquote) {
        border-color: #4b5563;
        color: #9ca3af;
    }
</style>
