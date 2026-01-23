<script lang="ts">
    import { goto } from "$app/navigation";
    import { onMount } from "svelte";
    import { Lock, User, AlertCircle } from "lucide-svelte";
    import { adminLogin, checkAdminAuth } from "$lib/api";

    let username = "";
    let password = "";
    let isLoading = false;
    let error = "";

    onMount(async () => {
        // Check if already logged in
        try {
            await checkAdminAuth();
            goto("/admin/dashboard");
        } catch {
            // Not logged in, stay on login page
        }
    });

    async function handleSubmit(event: Event) {
        event.preventDefault();

        if (!username.trim() || !password.trim()) return;

        isLoading = true;
        error = "";

        try {
            await adminLogin(username, password);
            goto("/admin/dashboard");
        } catch (err) {
            error = "Username atau password salah";
        } finally {
            isLoading = false;
        }
    }
</script>

<svelte:head>
    <title>Admin Login - Pradana Yahya</title>
</svelte:head>

<div class="min-h-[80vh] flex items-center justify-center px-4">
    <div class="w-full max-w-md">
        <div
            class="bg-white dark:bg-gray-800 rounded-2xl shadow-xl p-8 border border-gray-200 dark:border-gray-700"
        >
            <!-- Header -->
            <div class="text-center mb-8">
                <div
                    class="w-16 h-16 mx-auto mb-4 rounded-full bg-gradient-to-r from-sky-400 to-blue-600 flex items-center justify-center"
                >
                    <Lock class="w-8 h-8 text-white" />
                </div>
                <h1 class="text-2xl font-bold text-gray-900 dark:text-gray-50">
                    Admin Login
                </h1>
                <p class="text-gray-500 dark:text-gray-400 mt-2">
                    Masuk ke dashboard admin
                </p>
            </div>

            <!-- Form -->
            <form on:submit={handleSubmit} class="space-y-4">
                <div>
                    <label
                        for="username"
                        class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1"
                    >
                        Username
                    </label>
                    <div class="relative">
                        <User
                            class="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400"
                        />
                        <input
                            type="text"
                            id="username"
                            bind:value={username}
                            required
                            disabled={isLoading}
                            placeholder="Username"
                            class="w-full pl-10 pr-4 py-2.5 rounded-lg border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-900 dark:text-gray-100 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:opacity-50"
                        />
                    </div>
                </div>

                <div>
                    <label
                        for="password"
                        class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1"
                    >
                        Password
                    </label>
                    <div class="relative">
                        <Lock
                            class="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400"
                        />
                        <input
                            type="password"
                            id="password"
                            bind:value={password}
                            required
                            disabled={isLoading}
                            placeholder="Password"
                            class="w-full pl-10 pr-4 py-2.5 rounded-lg border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-900 dark:text-gray-100 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:opacity-50"
                        />
                    </div>
                </div>

                {#if error}
                    <div
                        class="flex items-center gap-2 p-3 rounded-lg bg-red-50 dark:bg-red-900/20 text-red-600 dark:text-red-400 text-sm"
                    >
                        <AlertCircle class="w-4 h-4 flex-shrink-0" />
                        {error}
                    </div>
                {/if}

                <button
                    type="submit"
                    disabled={isLoading || !username.trim() || !password.trim()}
                    class="w-full py-3 px-6 rounded-lg bg-gradient-to-r from-sky-400 to-blue-600 text-white font-medium hover:from-sky-500 hover:to-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed transition-all"
                >
                    {#if isLoading}
                        <span class="flex items-center justify-center gap-2">
                            <svg
                                class="animate-spin h-5 w-5"
                                fill="none"
                                viewBox="0 0 24 24"
                            >
                                <circle
                                    class="opacity-25"
                                    cx="12"
                                    cy="12"
                                    r="10"
                                    stroke="currentColor"
                                    stroke-width="4"
                                ></circle>
                                <path
                                    class="opacity-75"
                                    fill="currentColor"
                                    d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"
                                ></path>
                            </svg>
                            Memproses...
                        </span>
                    {:else}
                        Masuk
                    {/if}
                </button>
            </form>

            <p
                class="text-center text-sm text-gray-500 dark:text-gray-400 mt-6"
            >
                <a href="/" class="text-blue-500 hover:text-blue-600"
                    >← Kembali ke beranda</a
                >
            </p>
        </div>
    </div>
</div>
