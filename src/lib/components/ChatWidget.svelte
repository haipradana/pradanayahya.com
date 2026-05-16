<script lang="ts">
  import { onMount } from "svelte";
  import { MessageCircle, X, Send, Trash2 } from "lucide-svelte";
  import { sendChatMessage, getChatHistory } from "$lib/api";
  import { marked } from "marked";
  import DOMPurify from "dompurify";
  import { fade, fly } from "svelte/transition";
  import { cubicOut } from "svelte/easing";
  let isOpen = false;
  let messages: Array<{ role: "user" | "assistant"; content: string }> = [];
  let inputValue = "";
  let isLoading = false;
  let sessionId: string | null = null;
  let messagesContainer: HTMLDivElement;
  let isDarkMode = false;
  let chatVersion = 0;

  const quickActions = [
    {
      label: "🚀 Projects",
      message: "Apa saja project yang sudah dibuat Pradana?",
    },
    { label: "👋 Tentang Dana", message: "Ceritakan tentang Pradana" },
    { label: "💡 Skills", message: "Apa skill utama Pradana?" },
    { label: "📧 Contact", message: "Bagaimana cara menghubungi Pradana?" },
  ];

  onMount(() => {
    isDarkMode = document.documentElement.classList.contains("dark");

    const observer = new MutationObserver(() => {
      isDarkMode = document.documentElement.classList.contains("dark");
    });
    observer.observe(document.documentElement, {
      attributes: true,
      attributeFilter: ["class"],
    });

    const savedSession = localStorage.getItem("chat_session_id");
    if (savedSession) {
      sessionId = savedSession;
      loadChatHistory();
    }

    return () => observer.disconnect();
  });

  async function loadChatHistory() {
    if (!sessionId) return;
    try {
      const history = await getChatHistory(sessionId);
      messages = history.messages.map(
        (m: { role: string; content: string }) => ({
          role: m.role as "user" | "assistant",
          content: m.content,
        }),
      );
    } catch (error) {
      sessionId = null;
      localStorage.removeItem("chat_session_id");
    }
  }

  // Parse markdown and sanitize
  function parseMessage(content: string): string {
    const rawHtml = marked.parse(content) as string;
    return DOMPurify.sanitize(rawHtml);
  }

  async function sendMessage(text?: string) {
    const messageText = text || inputValue.trim();
    if (!messageText || isLoading) return;
    const currentChatVersion = chatVersion;

    messages = [...messages, { role: "user", content: messageText }];
    inputValue = "";
    isLoading = true;

    setTimeout(() => {
      if (messagesContainer)
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }, 10);

    try {
      const response = await sendChatMessage(
        messageText,
        sessionId || undefined,
      );
      if (currentChatVersion !== chatVersion) return;
      if (!sessionId) {
        sessionId = response.session_id;
        localStorage.setItem("chat_session_id", sessionId!);
      }
      messages = [...messages, { role: "assistant", content: response.answer }];
    } catch (error) {
      if (currentChatVersion !== chatVersion) return;
      messages = [
        ...messages,
        {
          role: "assistant",
          content: "Maaf, ada masalah teknis. Coba lagi nanti ya! 🙏",
        },
      ];
    } finally {
      if (currentChatVersion === chatVersion) {
        isLoading = false;
        setTimeout(() => {
          if (messagesContainer)
            messagesContainer.scrollTop = messagesContainer.scrollHeight;
        }, 10);
      }
    }
  }

  function handleKeyDown(event: KeyboardEvent) {
    if (event.key === "Enter" && !event.shiftKey) {
      event.preventDefault();
      sendMessage();
    }
  }

  function toggleChat() {
    isOpen = !isOpen;
  }

  function clearUserChat() {
    chatVersion += 1;
    messages = [];
    inputValue = "";
    sessionId = null;
    isLoading = false;
    localStorage.removeItem("chat_session_id");
  }
</script>

<!-- Floating Toggle Button -->
<button
  on:click={toggleChat}
  class="fixed bottom-6 right-6 z-50 w-12 h-12 rounded-full bg-ink-light text-surface-light dark:bg-ink-dark dark:text-surface-dark shadow-lg hover:shadow-xl transition-all duration-300 hover:-translate-y-0.5 flex items-center justify-center overflow-hidden ring-1 ring-ink-faint-light dark:ring-ink-faint-dark"
  aria-label="Toggle chat"
>
  {#if isOpen}
    <div
      in:fade={{ duration: 200 }}
      out:fade={{ duration: 200 }}
      class="absolute inset-0 flex items-center justify-center"
    >
      <X class="w-6 h-6" />
    </div>
  {:else}
    <div
      in:fade={{ duration: 200 }}
      out:fade={{ duration: 200 }}
      class="absolute inset-0 flex items-center justify-center"
    >
      <MessageCircle class="w-6 h-6" />
    </div>
  {/if}
</button>

<!-- Chat Window -->
{#if isOpen}
  <div
    transition:fly={{ y: 20, duration: 300, easing: cubicOut }}
    class="fixed bottom-24 right-6 z-50 w-[380px] sm:w-[480px] md:w-[550px] max-w-[calc(100vw-3rem)] h-[520px] sm:h-[600px] max-h-[calc(100vh-8rem)] bg-surface-light-elev dark:bg-surface-dark-elev rounded-3xl shadow-xl dark:shadow-2xl flex flex-col overflow-hidden border border-ink-faint-light dark:border-ink-faint-dark"
  >
    <!-- Header - Clean & Minimal -->
    <div
      class="px-5 py-4 border-b border-ink-faint-light dark:border-ink-faint-dark flex items-center justify-between"
    >
      <div class="flex items-center gap-3">
        <img
          src={isDarkMode
            ? "/images/logodana-dark.png"
            : "/images/logodana-light.png"}
          alt="Dana"
          class="w-12 h-12 object-contain"
        />
        <span
          class="text-xl font-bold text-gray-900 dark:text-white"
          style="font-family: 'Plus Jakarta Sans', sans-serif;">Latent</span
        >
      </div>
      <div class="flex items-center gap-1">
        <button
          type="button"
          on:click={clearUserChat}
          class="p-2 hover:bg-surface-light-muted dark:hover:bg-surface-dark-muted rounded-full transition-colors text-ink-muted-light dark:text-ink-muted-dark"
          aria-label="Hapus chat di browser"
          title="Hapus chat"
        >
          <Trash2 class="w-5 h-5" />
        </button>
        <button
          type="button"
          on:click={toggleChat}
          class="p-2 hover:bg-surface-light-muted dark:hover:bg-surface-dark-muted rounded-full transition-colors text-ink-muted-light dark:text-ink-muted-dark"
          aria-label="Tutup chat"
        >
          <X class="w-5 h-5" />
        </button>
      </div>
    </div>

    <!-- Messages Area -->
    <div
      bind:this={messagesContainer}
      class="flex-1 overflow-y-auto px-5 py-4 space-y-4"
    >
      {#if messages.length === 0}
        <!-- Welcome -->
        <div class="text-ink-muted-light dark:text-ink-muted-dark text-sm leading-relaxed">
          Hai! 👋 Aku <span class="font-medium">Latent</span>, asisten AI. Apa
          yang ingin kamu ketahui tentang Pradana?
        </div>

        <!-- Quick Actions -->
        <div class="pt-2">
          <div class="flex flex-wrap gap-2">
            {#each quickActions as action}
              <button
                on:click={() => sendMessage(action.message)}
                class="px-3 py-2 bg-surface-light-muted dark:bg-surface-dark-muted hover:border-accent-300 dark:hover:border-accent-700 border border-transparent text-ink-light dark:text-ink-dark text-sm rounded-xl transition-colors"
              >
                {action.label}
              </button>
            {/each}
          </div>
        </div>
      {:else}
        {#each messages as message}
          <div
            class={`flex ${message.role === "user" ? "justify-end" : "justify-start"}`}
          >
            <div
              class={`max-w-[85%] rounded-2xl px-4 py-2.5 text-sm leading-relaxed ${
                message.role === "user"
                  ? "bg-ink-light text-surface-light dark:bg-ink-dark dark:text-surface-dark"
                  : "bg-surface-light-muted dark:bg-surface-dark-muted text-ink-light dark:text-ink-dark markdown-content"
              }`}
            >
              {#if message.role === "assistant"}
                {@html parseMessage(message.content)}
              {:else}
                {message.content}
              {/if}
            </div>
          </div>
        {/each}

        {#if isLoading}
          <div class="flex justify-start">
            <div
              class="bg-surface-light-muted dark:bg-surface-dark-muted text-ink-muted-light dark:text-ink-muted-dark rounded-2xl px-4 py-2.5 text-sm"
            >
              <span class="inline-flex gap-1">
                <span class="animate-bounce">•</span>
                <span class="animate-bounce" style="animation-delay: 0.15s"
                  >•</span
                >
                <span class="animate-bounce" style="animation-delay: 0.3s"
                  >•</span
                >
              </span>
            </div>
          </div>
        {/if}
      {/if}
    </div>

    <!-- Input Area -->
    <div class="px-4 py-4 border-t border-ink-faint-light dark:border-ink-faint-dark">
      <div class="flex gap-2 items-center">
        <input
          type="text"
          bind:value={inputValue}
          on:keydown={handleKeyDown}
          placeholder="Tulis pesan..."
          disabled={isLoading}
          class="flex-1 bg-surface-light-muted dark:bg-surface-dark-muted text-ink-light dark:text-ink-dark placeholder:text-ink-muted-light/60 dark:placeholder:text-ink-muted-dark/60 rounded-xl px-4 py-3 text-sm border border-transparent focus:outline-none focus:border-accent-500 disabled:opacity-50 transition-colors"
        />
        <button
          on:click={() => sendMessage()}
          disabled={!inputValue.trim() || isLoading}
          class="w-11 h-11 rounded-xl bg-ink-light hover:opacity-90 text-surface-light dark:bg-ink-dark dark:text-surface-dark flex items-center justify-center transition-all disabled:opacity-40 disabled:cursor-not-allowed"
        >
          <Send class="w-5 h-5" />
        </button>
      </div>
    </div>
  </div>
{/if}

<style>
  @import url("https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700&display=swap");

  /* Markdown Styles for Chat */
  :global(.markdown-content p) {
    margin-bottom: 0.5rem;
  }
  :global(.markdown-content p:last-child) {
    margin-bottom: 0;
  }
  :global(.markdown-content a) {
    color: #059669;
    text-decoration: underline;
  }
  :global(.dark .markdown-content a) {
    color: #34d399;
  }
  :global(.markdown-content ul) {
    list-style-type: disc;
    margin-left: 1.25rem;
    margin-bottom: 0.5rem;
  }
  :global(.markdown-content ol) {
    list-style-type: decimal;
    margin-left: 1.25rem;
    margin-bottom: 0.5rem;
  }
  :global(.markdown-content strong) {
    font-weight: 600;
  }
</style>
