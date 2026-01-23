<script lang="ts">
    import { onMount } from "svelte";
    import { goto } from "$app/navigation";
    import {
        LogOut,
        RefreshCw,
        Mail,
        MessageCircle,
        Database,
        ChevronLeft,
        Trash2,
        Check,
        Eye,
    } from "lucide-svelte";
    import {
        checkAdminAuth,
        adminLogout,
        getContacts,
        getChats,
        getContact,
        getChat,
        markContactRead,
        deleteContact,
        deleteChat,
        getIngestStatus,
        syncToQdrant,
    } from "$lib/api";

    type Tab = "contacts" | "chats" | "data";

    let activeTab: Tab = "contacts";
    let isLoading = true;
    let contacts: any[] = [];
    let chats: any[] = [];
    let selectedContact: any = null;
    let selectedChat: any = null;
    let ingestStatus: any = null;
    let isSyncing = false;

    onMount(async () => {
        try {
            await checkAdminAuth();
            await loadData();
        } catch {
            goto("/admin");
        }
    });

    async function loadData() {
        isLoading = true;
        try {
            const [contactsData, chatsData, statusData] = await Promise.all([
                getContacts(),
                getChats(),
                getIngestStatus(),
            ]);
            contacts = contactsData;
            chats = chatsData;
            ingestStatus = statusData;
        } catch (error) {
            console.error("Failed to load data:", error);
        } finally {
            isLoading = false;
        }
    }

    async function handleLogout() {
        await adminLogout();
        goto("/admin");
    }

    async function viewContact(id: string) {
        const data = await getContact(id);
        selectedContact = data;
        if (!data.is_read) {
            await markContactRead(id);
            contacts = contacts.map((c) =>
                c.id === id ? { ...c, is_read: true } : c,
            );
        }
    }

    async function handleDeleteContact(id: string) {
        if (confirm("Hapus pesan ini?")) {
            await deleteContact(id);
            contacts = contacts.filter((c) => c.id !== id);
            selectedContact = null;
        }
    }

    async function viewChat(id: string) {
        const data = await getChat(id);
        selectedChat = data;
    }

    async function handleDeleteChat(id: string) {
        if (confirm("Hapus chat ini?")) {
            await deleteChat(id);
            chats = chats.filter((c) => c.id !== id);
            selectedChat = null;
        }
    }

    async function handleSync() {
        if (
            confirm(
                "Sync semua data ke Qdrant? Ini akan menghapus data lama dan re-ingest.",
            )
        ) {
            isSyncing = true;
            try {
                await syncToQdrant();
                ingestStatus = await getIngestStatus();
                alert("Sync berhasil!");
            } catch (error) {
                alert("Sync gagal: " + error);
            } finally {
                isSyncing = false;
            }
        }
    }

    function formatDate(dateString: string) {
        return new Date(dateString).toLocaleString("id-ID", {
            day: "2-digit",
            month: "2-digit",
            year: "2-digit",
            hour: "2-digit",
            minute: "2-digit",
        });
    }
</script>

<svelte:head>
    <title>Dashboard - Admin</title>
</svelte:head>

<div class="min-h-screen bg-gray-100 dark:bg-gray-900">
    <!-- Header -->
    <header class="bg-white dark:bg-gray-800 shadow">
        <div
            class="max-w-7xl mx-auto px-4 py-4 flex items-center justify-between"
        >
            <div class="flex items-center gap-4">
                <a
                    href="/"
                    class="text-gray-500 hover:text-gray-700 dark:hover:text-gray-300"
                >
                    <ChevronLeft class="w-5 h-5" />
                </a>
                <h1 class="text-xl font-bold text-gray-900 dark:text-gray-50">
                    Pesan Masuk
                </h1>
                <span class="text-sm text-gray-500"
                    >Kelola pesan dari pengunjung website</span
                >
            </div>
            <div class="flex items-center gap-2">
                <button
                    on:click={loadData}
                    class="p-2 text-gray-600 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-100 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-lg transition-colors"
                >
                    <RefreshCw class="w-5 h-5" />
                </button>
                <button
                    on:click={handleLogout}
                    class="flex items-center gap-2 px-4 py-2 text-sm text-gray-600 hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-100 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-lg transition-colors"
                >
                    <LogOut class="w-4 h-4" />
                    Logout
                </button>
            </div>
        </div>
    </header>

    <!-- Tabs -->
    <div class="max-w-7xl mx-auto px-4 mt-4">
        <div class="flex gap-2">
            <button
                on:click={() => {
                    activeTab = "contacts";
                    selectedContact = null;
                }}
                class={`flex items-center gap-2 px-4 py-2 rounded-lg font-medium transition-colors ${
                    activeTab === "contacts"
                        ? "bg-gray-900 dark:bg-gray-100 text-white dark:text-gray-900"
                        : "bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-700"
                }`}
            >
                <Mail class="w-4 h-4" />
                CONTACT FORM
                <span
                    class="bg-gray-200 dark:bg-gray-600 text-gray-700 dark:text-gray-300 text-xs px-2 py-0.5 rounded-full"
                >
                    {contacts.length}
                </span>
            </button>
            <button
                on:click={() => {
                    activeTab = "chats";
                    selectedChat = null;
                }}
                class={`flex items-center gap-2 px-4 py-2 rounded-lg font-medium transition-colors ${
                    activeTab === "chats"
                        ? "bg-gray-900 dark:bg-gray-100 text-white dark:text-gray-900"
                        : "bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-700"
                }`}
            >
                <MessageCircle class="w-4 h-4" />
                AI CHAT
                <span
                    class="bg-orange-500 text-white text-xs px-2 py-0.5 rounded-full"
                >
                    {chats.length}
                </span>
            </button>
            <button
                on:click={() => (activeTab = "data")}
                class={`flex items-center gap-2 px-4 py-2 rounded-lg font-medium transition-colors ${
                    activeTab === "data"
                        ? "bg-gray-900 dark:bg-gray-100 text-white dark:text-gray-900"
                        : "bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-700"
                }`}
            >
                <Database class="w-4 h-4" />
                DATA SYNC
            </button>
        </div>
    </div>

    <!-- Content -->
    <div class="max-w-7xl mx-auto px-4 py-4">
        {#if isLoading}
            <div class="flex items-center justify-center py-20">
                <div
                    class="animate-spin rounded-full h-8 w-8 border-b-2 border-pink-500"
                ></div>
            </div>
        {:else if activeTab === "contacts"}
            <!-- Contacts Tab -->
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-4">
                <!-- List -->
                <div
                    class="bg-white dark:bg-gray-800 rounded-xl shadow overflow-hidden"
                >
                    <div class="p-4 border-b dark:border-gray-700">
                        <h2
                            class="font-semibold text-gray-900 dark:text-gray-100"
                        >
                            Percakapan
                        </h2>
                    </div>
                    <div
                        class="divide-y dark:divide-gray-700 max-h-[60vh] overflow-y-auto"
                    >
                        {#each contacts as contact}
                            <button
                                on:click={() => viewContact(contact.id)}
                                class={`w-full p-4 text-left hover:bg-gray-50 dark:hover:bg-gray-700 transition-colors ${
                                    selectedContact?.id === contact.id
                                        ? "bg-blue-50 dark:bg-blue-900/20"
                                        : ""
                                }`}
                            >
                                <div class="flex items-start justify-between">
                                    <div class="flex-1 min-w-0">
                                        <p
                                            class={`font-medium truncate ${contact.is_read ? "text-gray-600 dark:text-gray-400" : "text-gray-900 dark:text-gray-100"}`}
                                        >
                                            {contact.name}
                                        </p>
                                        <p
                                            class="text-sm text-gray-500 truncate"
                                        >
                                            {contact.message_preview}
                                        </p>
                                        <p class="text-xs text-gray-400 mt-1">
                                            {formatDate(contact.created_at)}
                                        </p>
                                    </div>
                                    {#if !contact.is_read}
                                        <span
                                            class="w-2 h-2 rounded-full bg-blue-500 flex-shrink-0 mt-2"
                                        ></span>
                                    {/if}
                                </div>
                            </button>
                        {:else}
                            <p class="p-4 text-gray-500 text-center">
                                Belum ada pesan
                            </p>
                        {/each}
                    </div>
                </div>

                <!-- Detail -->
                <div
                    class="lg:col-span-2 bg-white dark:bg-gray-800 rounded-xl shadow"
                >
                    <div
                        class="p-4 border-b dark:border-gray-700 flex items-center justify-between"
                    >
                        <h2
                            class="font-semibold text-gray-900 dark:text-gray-100"
                        >
                            Detail Pesan
                        </h2>
                        {#if selectedContact}
                            <button
                                on:click={() =>
                                    handleDeleteContact(selectedContact.id)}
                                class="text-red-500 hover:text-red-600 text-sm flex items-center gap-1"
                            >
                                <Trash2 class="w-4 h-4" />
                                Hapus
                            </button>
                        {/if}
                    </div>
                    <div class="p-4">
                        {#if selectedContact}
                            <div class="space-y-4">
                                <div>
                                    <label class="text-sm text-gray-500"
                                        >Dari</label
                                    >
                                    <p
                                        class="font-medium text-gray-900 dark:text-gray-100"
                                    >
                                        {selectedContact.name}
                                    </p>
                                </div>
                                <div>
                                    <label class="text-sm text-gray-500"
                                        >Email</label
                                    >
                                    <p class="text-gray-900 dark:text-gray-100">
                                        <a
                                            href="mailto:{selectedContact.email}"
                                            class="text-blue-500 hover:underline"
                                        >
                                            {selectedContact.email}
                                        </a>
                                    </p>
                                </div>
                                <div>
                                    <label class="text-sm text-gray-500"
                                        >Waktu</label
                                    >
                                    <p class="text-gray-900 dark:text-gray-100">
                                        {formatDate(selectedContact.created_at)}
                                    </p>
                                </div>
                                <div>
                                    <label class="text-sm text-gray-500"
                                        >Pesan</label
                                    >
                                    <div
                                        class="mt-2 p-4 bg-gray-50 dark:bg-gray-700 rounded-lg"
                                    >
                                        <p
                                            class="text-gray-900 dark:text-gray-100 whitespace-pre-wrap"
                                        >
                                            {selectedContact.message}
                                        </p>
                                    </div>
                                </div>
                            </div>
                        {:else}
                            <p class="text-gray-500 text-center py-10">
                                Pilih pesan untuk melihat detail
                            </p>
                        {/if}
                    </div>
                </div>
            </div>
        {:else if activeTab === "chats"}
            <!-- Chats Tab -->
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-4">
                <!-- List -->
                <div
                    class="bg-white dark:bg-gray-800 rounded-xl shadow overflow-hidden"
                >
                    <div class="p-4 border-b dark:border-gray-700">
                        <h2
                            class="font-semibold text-gray-900 dark:text-gray-100"
                        >
                            Percakapan
                        </h2>
                    </div>
                    <div
                        class="divide-y dark:divide-gray-700 max-h-[60vh] overflow-y-auto"
                    >
                        {#each chats as chat}
                            <button
                                on:click={() => viewChat(chat.id)}
                                class={`w-full p-4 text-left hover:bg-gray-50 dark:hover:bg-gray-700 transition-colors ${
                                    selectedChat?.id === chat.id
                                        ? "bg-blue-50 dark:bg-blue-900/20"
                                        : ""
                                }`}
                            >
                                <div class="flex items-start justify-between">
                                    <div class="flex-1 min-w-0">
                                        <p
                                            class="text-sm text-gray-500 font-mono truncate"
                                        >
                                            {chat.id.substring(0, 8)}...
                                        </p>
                                        <p
                                            class="text-sm text-gray-700 dark:text-gray-300 truncate"
                                        >
                                            {chat.preview}
                                        </p>
                                        <p class="text-xs text-gray-400 mt-1">
                                            {formatDate(chat.created_at)}
                                        </p>
                                    </div>
                                    <span
                                        class="text-xs bg-orange-100 dark:bg-orange-900/30 text-orange-600 dark:text-orange-400 px-2 py-0.5 rounded-full"
                                    >
                                        {chat.message_count} pesan
                                    </span>
                                </div>
                            </button>
                        {:else}
                            <p class="p-4 text-gray-500 text-center">
                                Belum ada chat
                            </p>
                        {/each}
                    </div>
                </div>

                <!-- Detail -->
                <div
                    class="lg:col-span-2 bg-white dark:bg-gray-800 rounded-xl shadow"
                >
                    <div
                        class="p-4 border-b dark:border-gray-700 flex items-center justify-between"
                    >
                        <h2
                            class="font-semibold text-gray-900 dark:text-gray-100"
                        >
                            Detail Percakapan
                        </h2>
                        {#if selectedChat}
                            <button
                                on:click={() =>
                                    handleDeleteChat(selectedChat.id)}
                                class="text-red-500 hover:text-red-600 text-sm flex items-center gap-1"
                            >
                                <Trash2 class="w-4 h-4" />
                                Hapus
                            </button>
                        {/if}
                    </div>
                    <div class="p-4 max-h-[60vh] overflow-y-auto">
                        {#if selectedChat}
                            <div class="space-y-4">
                                {#each selectedChat.messages as message}
                                    <div
                                        class={`flex ${message.role === "user" ? "justify-end" : "justify-start"}`}
                                    >
                                        <div
                                            class={`max-w-[80%] rounded-2xl px-4 py-2 ${
                                                message.role === "user"
                                                    ? "bg-gradient-to-r from-orange-500 to-pink-500 text-white rounded-br-md"
                                                    : "bg-gray-100 dark:bg-gray-700 text-gray-900 dark:text-gray-100 rounded-bl-md"
                                            }`}
                                        >
                                            <p
                                                class="text-sm whitespace-pre-wrap"
                                            >
                                                {message.content}
                                            </p>
                                            <p class="text-xs opacity-60 mt-1">
                                                {formatDate(message.created_at)}
                                            </p>
                                        </div>
                                    </div>
                                {/each}
                            </div>
                        {:else}
                            <p class="text-gray-500 text-center py-10">
                                Pilih chat untuk melihat detail
                            </p>
                        {/if}
                    </div>
                </div>
            </div>
        {:else if activeTab === "data"}
            <!-- Data Sync Tab -->
            <div class="bg-white dark:bg-gray-800 rounded-xl shadow p-6">
                <div class="flex items-center justify-between mb-6">
                    <div>
                        <h2
                            class="text-lg font-semibold text-gray-900 dark:text-gray-100"
                        >
                            Data Sync Status
                        </h2>
                        <p class="text-sm text-gray-500">
                            Kelola data portfolio untuk RAG chatbot
                        </p>
                    </div>
                    <button
                        on:click={handleSync}
                        disabled={isSyncing}
                        class="flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-pink-500 to-purple-600 text-white rounded-lg hover:from-pink-600 hover:to-purple-700 disabled:opacity-50 transition-all"
                    >
                        {#if isSyncing}
                            <svg
                                class="animate-spin h-4 w-4"
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
                            Syncing...
                        {:else}
                            <Database class="w-4 h-4" />
                            Sync to Qdrant
                        {/if}
                    </button>
                </div>

                {#if ingestStatus}
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
                        <div class="p-4 bg-gray-50 dark:bg-gray-700 rounded-lg">
                            <p class="text-sm text-gray-500">Total Points</p>
                            <p
                                class="text-2xl font-bold text-gray-900 dark:text-gray-100"
                            >
                                {ingestStatus.total_points}
                            </p>
                        </div>
                        <div class="p-4 bg-gray-50 dark:bg-gray-700 rounded-lg">
                            <p class="text-sm text-gray-500">
                                Collection Status
                            </p>
                            <p class="text-lg font-medium text-green-600">
                                {ingestStatus.collection_status}
                            </p>
                        </div>
                        <div class="p-4 bg-gray-50 dark:bg-gray-700 rounded-lg">
                            <p class="text-sm text-gray-500">Last Sync</p>
                            <p class="text-sm text-gray-900 dark:text-gray-100">
                                {ingestStatus.last_sync
                                    ? formatDate(ingestStatus.last_sync)
                                    : "Never"}
                            </p>
                        </div>
                    </div>

                    <div>
                        <h3
                            class="font-medium text-gray-900 dark:text-gray-100 mb-3"
                        >
                            Data Files
                        </h3>
                        <div class="space-y-2">
                            {#each ingestStatus.files || [] as file}
                                <div
                                    class="flex items-center justify-between p-3 bg-gray-50 dark:bg-gray-700 rounded-lg"
                                >
                                    <span
                                        class="font-mono text-sm text-gray-700 dark:text-gray-300"
                                        >{file.filename}</span
                                    >
                                    <span class="text-sm text-gray-500"
                                        >{file.item_count} items</span
                                    >
                                </div>
                            {:else}
                                <p class="text-gray-500 text-sm">
                                    No data files found
                                </p>
                            {/each}
                        </div>
                    </div>
                {/if}

                <div class="mt-6 p-4 bg-blue-50 dark:bg-blue-900/20 rounded-lg">
                    <p class="text-sm text-blue-700 dark:text-blue-400">
                        💡 <strong>Tip:</strong> Data files terletak di
                        <code>portfolio-backend/data/portfolio/</code>. Edit
                        JSON files tersebut lalu klik "Sync to Qdrant" untuk
                        update chatbot knowledge.
                    </p>
                </div>
            </div>
        {/if}
    </div>
</div>
