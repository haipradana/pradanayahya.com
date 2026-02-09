export interface BlogPost {
    slug: string;
    title: string;
    date: string;
    category: string;
    content: string;
    draft?: boolean;
}

export const blogPosts: BlogPost[] = [
    {
        slug: "hello-world",
        title: "Hello World!",
        date: "2026-02-09",
        category: "General",
        content: `
# Hello World!

Welcome to my blog! This is my first post where I'll be sharing my thoughts, learnings, and experiences in the world of technology.

## What to Expect

I'll be writing about:
- **Machine Learning** and **Deep Learning** experiments
- **Natural Language Processing** projects
- **Computer Vision** explorations
- General tech musings and learnings

Stay tuned for more posts!
    `.trim(),
    },
];

// Helper function to format date like "Feb 9, 2026"
export function formatDate(dateStr: string): string {
    const date = new Date(dateStr);
    return date.toLocaleDateString('en-US', {
        month: 'short',
        day: 'numeric',
        year: 'numeric'
    });
}

// Helper function to get year from date
export function getYear(dateStr: string): number {
    return new Date(dateStr).getFullYear();
}

// Group posts by year
export function groupPostsByYear(posts: BlogPost[]): Map<number, BlogPost[]> {
    const grouped = new Map<number, BlogPost[]>();

    // Filter out drafts and sort by date (newest first)
    const publishedPosts = posts
        .filter(post => !post.draft)
        .sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime());

    for (const post of publishedPosts) {
        const year = getYear(post.date);
        if (!grouped.has(year)) {
            grouped.set(year, []);
        }
        grouped.get(year)!.push(post);
    }

    return grouped;
}

// Get unique categories
export function getCategories(posts: BlogPost[]): string[] {
    const categories = new Set(posts.map(p => p.category));
    return [...categories].sort();
}
