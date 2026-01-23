<script lang="ts">
  import {
    Mail,
    Linkedin,
    Github,
    Instagram,
    Send,
    CheckCircle,
    AlertCircle,
  } from "lucide-svelte";
  import { submitContact } from "$lib/api";

  let name = "";
  let email = "";
  let message = "";
  let isSubmitting = false;
  let submitStatus: "idle" | "success" | "error" = "idle";
  let errorMessage = "";

  async function handleSubmit(event: Event) {
    event.preventDefault();

    if (!name.trim() || !email.trim() || !message.trim()) return;

    isSubmitting = true;
    submitStatus = "idle";

    try {
      await submitContact({ name, email, message });
      submitStatus = "success";
      name = "";
      email = "";
      message = "";

      // Reset status after 5 seconds
      setTimeout(() => {
        submitStatus = "idle";
      }, 5000);
    } catch (error) {
      submitStatus = "error";
      errorMessage = "Gagal mengirim pesan. Coba lagi nanti.";
    } finally {
      isSubmitting = false;
    }
  }
</script>

<svelte:head>
  <title>Reach Me! - Pradana Yahya</title>
  <meta
    name="description"
    content="Get in touch with Pradana Yahya - Developer and Tech Enthusiast"
  />
</svelte:head>

<div class="max-w-2xl mx-auto px-6 sm:px-20 py-8 sm:py-16">
  <!-- Header -->
  <section class="text-center mb-8 sm:mb-12">
    <h1
      class="text-xl sm:text-2xl lg:text-3xl xl:text-4xl font-bold text-gray-900 dark:text-gray-50 mb-4"
    >
      Reach Me!
    </h1>
  </section>

  <!-- Contact Links -->
  <section class="space-y-4 sm:space-y-6">
    <!-- Email -->
    <div class="flex items-center justify-start">
      <a
        href="mailto:pradanayahyaabdillah@mail.ugm.ac.id"
        class="flex items-center space-x-2 sm:space-x-3 text-sm sm:text-lg text-gray-700 dark:text-gray-300 hover:text-red-500 dark:hover:text-red-400 transition-colors group"
      >
        <div
          class="p-1.5 sm:p-2 bg-red-100 dark:bg-red-900/20 rounded-lg group-hover:bg-red-200 dark:group-hover:bg-red-900/30 transition-colors"
        >
          <Mail class="w-4 h-4 sm:w-5 sm:h-5 text-red-600 dark:text-red-400" />
        </div>
        <span class="underline break-all sm:break-normal"
          >pradanayahyaabdillah@mail.ugm.ac.id</span
        >
      </a>
    </div>

    <!-- LinkedIn -->
    <div class="flex items-center justify-start">
      <a
        href="https://www.linkedin.com/in/pradana-yahya/"
        target="_blank"
        rel="noopener noreferrer"
        class="flex items-center space-x-2 sm:space-x-3 text-sm sm:text-lg text-gray-700 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-500 transition-colors group"
      >
        <div
          class="p-1.5 sm:p-2 bg-blue-100 dark:bg-blue-900/20 rounded-lg group-hover:bg-blue-200 dark:group-hover:bg-blue-900/30 transition-colors"
        >
          <Linkedin
            class="w-4 h-4 sm:w-5 sm:h-5 text-blue-700 dark:text-blue-500"
          />
        </div>
        <span class="underline">Pradana Yahya Abdillah</span>
      </a>
    </div>

    <!-- GitHub -->
    <div class="flex items-center justify-start">
      <a
        href="https://github.com/haipradana"
        target="_blank"
        rel="noopener noreferrer"
        class="flex items-center space-x-2 sm:space-x-3 text-sm sm:text-lg text-gray-700 dark:text-gray-300 hover:text-gray-800 dark:hover:text-gray-200 transition-colors group"
      >
        <div
          class="p-1.5 sm:p-2 bg-gray-100 dark:bg-gray-900/20 rounded-lg group-hover:bg-gray-200 dark:group-hover:bg-gray-900/30 transition-colors"
        >
          <Github
            class="w-4 h-4 sm:w-5 sm:h-5 text-gray-800 dark:text-gray-200"
          />
        </div>
        <span class="underline">haipradana</span>
      </a>
    </div>

    <!-- Hugging Face -->
    <div class="flex items-center justify-start">
      <a
        href="https://huggingface.co/haipradana"
        target="_blank"
        rel="noopener noreferrer"
        class="flex items-center space-x-2 sm:space-x-3 text-sm sm:text-lg text-gray-700 dark:text-gray-300 hover:text-yellow-500 dark:hover:text-yellow-400 transition-colors group"
      >
        <div
          class="p-1.5 sm:p-2 bg-yellow-100 dark:bg-yellow-900/20 rounded-lg group-hover:bg-yellow-200 dark:group-hover:bg-yellow-900/30 transition-colors"
        >
          <svg
            class="w-4 h-4 sm:w-5 sm:h-5 text-yellow-600 dark:text-yellow-400"
            viewBox="0 0 24 24"
            fill="currentColor"
          >
            <path
              d="M1.4446 11.5059c0 1.1021 0.1673 2.1585 0.4847 3.1563 -0.0378 -0.0028 -0.0691 -0.0058 -0.1058 -0.0058 -0.4209 0 -0.8015 0.16 -1.0704 0.4512 -0.3454 0.3737 -0.4984 0.8335 -0.4316 1.293a1.576 1.576 0 0 0 0.2148 0.5978c-0.2319 0.1864 -0.4018 0.4456 -0.4844 0.7578 -0.0646 0.2448 -0.131 0.7543 0.2149 1.2794a1.4552 1.4552 0 0 0 -0.0625 0.1055c-0.208 0.3923 -0.2207 0.8372 -0.0371 1.25 0.2783 0.6258 0.9696 1.1175 2.3126 1.6467 0.8356 0.3292 1.5988 0.5411 1.6056 0.543 1.1046 0.2847 2.104 0.4277 2.969 0.4277 1.4173 0 2.4754 -0.3849 3.1525 -1.1446 1.538 0.2651 2.791 0.1403 3.592 0.006 0.6773 0.7555 1.7332 1.1387 3.1467 1.1387 0.8649 0 1.8643 -0.143 2.969 -0.4278 0.0068 -0.0019 0.77 -0.2138 1.6056 -0.543 1.343 -0.5292 2.0343 -1.0208 2.3126 -1.6466 0.1836 -0.4129 0.171 -0.8577 -0.037 -1.25a1.4685 1.4685 0 0 0 -0.0626 -0.1056c0.346 -0.525 0.2795 -1.0346 0.2149 -1.2793 -0.0826 -0.3122 -0.2525 -0.5714 -0.4844 -0.7579 0.11 -0.1816 0.1831 -0.3788 0.2148 -0.5977 0.0669 -0.4595 -0.0862 -0.9193 -0.4316 -1.293 -0.2688 -0.2913 -0.6495 -0.4513 -1.0704 -0.4513 -0.0209 0 -0.0376 0.0008 -0.0588 0.0018 0.3162 -0.9966 0.4846 -2.0518 0.4846 -3.1523 0 -5.807 -4.7362 -10.5144 -10.5789 -10.5144 -5.8426 0 -10.5788 4.7073 -10.5788 10.5144Zm10.5788 -9.4831c5.2727 0 9.5476 4.246 9.5476 9.483a9.4201 9.4201 0 0 1 -0.2696 2.2365c-0.0039 -0.0047 -0.0079 -0.011 -0.0117 -0.0156 -0.274 -0.3255 -0.6679 -0.5059 -1.1075 -0.5059 -0.352 0 -0.714 0.1155 -1.0763 0.3438 -0.2403 0.1517 -0.5058 0.422 -0.7793 0.7598 -0.2534 -0.3492 -0.608 -0.5832 -1.0137 -0.6465a1.5174 1.5174 0 0 0 -0.2344 -0.0176c-0.9263 0 -1.4828 0.7993 -1.6935 1.5177 -0.1046 0.2426 -0.6065 1.3482 -1.3614 2.0978 -1.1681 1.1601 -1.4458 2.3534 -0.8396 3.6382 -0.843 0.1029 -1.5836 0.0927 -2.365 -0.006 0.5906 -1.212 0.3626 -2.4388 -0.8426 -3.6322 -0.755 -0.7496 -1.2568 -1.8552 -1.3614 -2.0978 -0.2107 -0.7184 -0.7673 -1.5177 -1.6935 -1.5177 -0.078 0 -0.1568 0.0054 -0.2344 0.0176 -0.4057 0.0633 -0.7604 0.2973 -1.0137 0.6465 -0.2735 -0.3379 -0.539 -0.6081 -0.7794 -0.7598 -0.3622 -0.2283 -0.7243 -0.3438 -1.0762 -0.3438 -0.4266 0 -0.8094 0.171 -1.0821 0.4786a9.4208 9.4208 0 0 1 -0.2598 -2.1936c0 -5.237 4.2749 -9.483 9.5475 -9.483z"
            />
          </svg>
        </div>
        <span class="underline">haipradana</span>
      </a>
    </div>

    <!-- Instagram -->
    <div class="flex items-center justify-start">
      <a
        href="https://instagram.com/pradanaabdillah"
        target="_blank"
        rel="noopener noreferrer"
        class="flex items-center space-x-2 sm:space-x-3 text-sm sm:text-lg text-gray-700 dark:text-gray-300 hover:text-pink-500 dark:hover:text-pink-400 transition-colors group"
      >
        <div
          class="p-1.5 sm:p-2 bg-gradient-to-br from-pink-100 to-purple-100 dark:from-pink-900/20 dark:to-purple-900/20 rounded-lg group-hover:from-pink-200 group-hover:to-purple-200 dark:group-hover:from-pink-900/30 dark:group-hover:to-purple-900/30 transition-colors"
        >
          <Instagram
            class="w-4 h-4 sm:w-5 sm:h-5 text-pink-600 dark:text-pink-400"
          />
        </div>
        <span class="underline">pradanaabdillah</span>
      </a>
    </div>
  </section>

  <!-- Divider -->
  <div class="my-8 sm:my-12 flex items-center gap-4">
    <div class="flex-1 h-px bg-gray-200 dark:bg-gray-700"></div>
    <span class="text-sm text-gray-500 dark:text-gray-400"
      >atau kirim pesan langsung</span
    >
    <div class="flex-1 h-px bg-gray-200 dark:bg-gray-700"></div>
  </div>

  <!-- Contact Form -->
  <section>
    <h2
      class="text-lg sm:text-xl font-semibold text-gray-900 dark:text-gray-50 mb-6 flex items-center gap-2"
    >
      <Send class="w-5 h-5" />
      Kirim Pesan
    </h2>

    <form on:submit={handleSubmit} class="space-y-4">
      <!-- Name -->
      <div>
        <label
          for="name"
          class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1"
        >
          Nama
        </label>
        <input
          type="text"
          id="name"
          bind:value={name}
          required
          disabled={isSubmitting}
          placeholder="Nama kamu"
          class="w-full px-4 py-2.5 rounded-lg border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100 placeholder-gray-400 dark:placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500 dark:focus:ring-blue-400 focus:border-transparent disabled:opacity-50 transition-colors"
        />
      </div>

      <!-- Email -->
      <div>
        <label
          for="email"
          class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1"
        >
          Email
        </label>
        <input
          type="email"
          id="email"
          bind:value={email}
          required
          disabled={isSubmitting}
          placeholder="email@example.com"
          class="w-full px-4 py-2.5 rounded-lg border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100 placeholder-gray-400 dark:placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500 dark:focus:ring-blue-400 focus:border-transparent disabled:opacity-50 transition-colors"
        />
      </div>

      <!-- Message -->
      <div>
        <label
          for="message"
          class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1"
        >
          Pesan
        </label>
        <textarea
          id="message"
          bind:value={message}
          required
          disabled={isSubmitting}
          rows="4"
          placeholder="Tulis pesan kamu di sini..."
          class="w-full px-4 py-2.5 rounded-lg border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100 placeholder-gray-400 dark:placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-blue-500 dark:focus:ring-blue-400 focus:border-transparent disabled:opacity-50 transition-colors resize-none"
        ></textarea>
      </div>

      <!-- Submit Button -->
      <button
        type="submit"
        disabled={isSubmitting ||
          !name.trim() ||
          !email.trim() ||
          !message.trim()}
        class="w-full py-3 px-6 rounded-lg bg-gradient-to-r from-sky-500 to-blue-600 text-white font-medium hover:from-sky-600 hover:to-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 dark:focus:ring-offset-gray-900 disabled:opacity-50 disabled:cursor-not-allowed transition-all flex items-center justify-center gap-2"
      >
        {#if isSubmitting}
          <svg
            class="animate-spin h-5 w-5"
            xmlns="http://www.w3.org/2000/svg"
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
              d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
            ></path>
          </svg>
          Mengirim...
        {:else}
          <Send class="w-5 h-5" />
          Kirim Pesan
        {/if}
      </button>

      <!-- Status Messages -->
      {#if submitStatus === "success"}
        <div
          class="flex items-center gap-2 p-4 rounded-lg bg-green-50 dark:bg-green-900/20 text-green-700 dark:text-green-400"
        >
          <CheckCircle class="w-5 h-5 flex-shrink-0" />
          <p>Pesan berhasil dikirim! Terima kasih sudah menghubungi saya. 🙏</p>
        </div>
      {/if}

      {#if submitStatus === "error"}
        <div
          class="flex items-center gap-2 p-4 rounded-lg bg-red-50 dark:bg-red-900/20 text-red-700 dark:text-red-400"
        >
          <AlertCircle class="w-5 h-5 flex-shrink-0" />
          <p>{errorMessage}</p>
        </div>
      {/if}
    </form>
  </section>
</div>
