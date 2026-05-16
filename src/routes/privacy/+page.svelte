<script lang="ts">
  const lastUpdated = '17 May 2026';
  const contactEmail = 'pradana@pradanayahya.com';
</script>

<svelte:head>
  <title>Privacy Policy — Pradana Yahya</title>
  <meta
    name="description"
    content="Privacy policy for pradanayahya.com — what data is collected, how it is used, and how to opt out."
  />
</svelte:head>

<section class="mx-auto max-w-3xl px-5 sm:px-8 pt-14 lg:pt-20 pb-10">
  <p class="eyebrow">Legal</p>
  <h1 class="font-display text-4xl lg:text-5xl mt-3 text-ink-light dark:text-ink-dark text-balance">
    Privacy Policy
  </h1>
  <p class="mt-3 text-sm text-ink-muted-light dark:text-ink-muted-dark">
    Last updated: {lastUpdated}
  </p>
</section>

<section class="mx-auto max-w-3xl px-5 sm:px-8 pb-24 space-y-8 text-[15px] leading-relaxed text-ink-light/85 dark:text-ink-dark/85">
  <p>
    This Privacy Policy explains how <strong>pradanayahya.com</strong>
    (“the site”, “we”) handles information when you visit. The site is a
    personal portfolio operated by Pradana Yahya Abdillah from Yogyakarta,
    Indonesia. By using the site you agree to the practices described
    below.
  </p>

  <div>
    <h2 class="font-display text-2xl text-ink-light dark:text-ink-dark mb-3">
      1. Information we collect
    </h2>
    <ul class="list-disc pl-5 space-y-2">
      <li>
        <strong>Contact form.</strong> If you submit the form on
        <a class="underline decoration-accent-500 underline-offset-4" href="/contact">/contact</a>,
        we receive the name, email address, and message you provide. We use
        this only to reply to your message and store it on our backend
        database.
      </li>
      <li>
        <strong>RAG chat assistant.</strong> The chat widget sends your
        message to our backend so an AI assistant can answer questions
        about Pradana. A random <code>chat_session_id</code> is stored in
        your browser’s <code>localStorage</code> so the conversation
        persists across reloads. You can clear it at any time from the
        chat menu (trash icon) or by clearing site data in your browser.
      </li>
      <li>
        <strong>Theme preference.</strong> Your light/dark mode choice is
        stored in <code>localStorage</code> as <code>theme</code>.
      </li>
      <li>
        <strong>Server logs.</strong> Our hosting providers (Netlify and
        our backend host) automatically log standard request data — IP
        address, user agent, referrer, and timestamp — to operate the
        service and prevent abuse.
      </li>
      <li>
        <strong>Analytics &amp; Ads.</strong> We may use Google services
        such as Google Search Console, Google Analytics, and Google
        AdSense. These third parties may use cookies and similar
        technologies to serve ads based on your visits to this and other
        sites. You can opt out of personalised advertising at
        <a class="underline decoration-accent-500 underline-offset-4" href="https://www.google.com/settings/ads" target="_blank" rel="noopener noreferrer">google.com/settings/ads</a>
        and learn more at
        <a class="underline decoration-accent-500 underline-offset-4" href="https://policies.google.com/technologies/ads" target="_blank" rel="noopener noreferrer">policies.google.com/technologies/ads</a>.
      </li>
    </ul>
  </div>

  <div>
    <h2 class="font-display text-2xl text-ink-light dark:text-ink-dark mb-3">
      2. How we use information
    </h2>
    <ul class="list-disc pl-5 space-y-2">
      <li>Reply to messages you send through the contact form or chat.</li>
      <li>Improve content and navigation based on aggregate, anonymised usage.</li>
      <li>Detect and prevent abuse of the site or backend services.</li>
    </ul>
    <p class="mt-3">
      We do not sell your personal information. We do not use your data
      to train external models.
    </p>
  </div>

  <div>
    <h2 class="font-display text-2xl text-ink-light dark:text-ink-dark mb-3">
      3. Cookies &amp; local storage
    </h2>
    <p>
      The site itself does not set first-party tracking cookies. It uses
      <code>localStorage</code> only for the items above (theme,
      <code>chat_session_id</code>). Third-party services (e.g. Google
      AdSense, Google Analytics) may set their own cookies if enabled —
      please refer to their policies.
    </p>
  </div>

  <div>
    <h2 class="font-display text-2xl text-ink-light dark:text-ink-dark mb-3">
      4. Data retention
    </h2>
    <p>
      Contact-form submissions are retained until they are no longer
      needed to respond to your inquiry. Server logs are retained for the
      period our infrastructure providers default to (typically up to 90
      days). You may request deletion at any time.
    </p>
  </div>

  <div>
    <h2 class="font-display text-2xl text-ink-light dark:text-ink-dark mb-3">
      5. Your rights
    </h2>
    <p>
      You can request access to, correction of, or deletion of any
      personal information we hold about you by emailing
      <a class="underline decoration-accent-500 underline-offset-4" href={`mailto:${contactEmail}`}>{contactEmail}</a>.
      Depending on your jurisdiction (GDPR, UU PDP, etc.), additional
      rights may apply.
    </p>
  </div>

  <div>
    <h2 class="font-display text-2xl text-ink-light dark:text-ink-dark mb-3">
      6. Children
    </h2>
    <p>
      The site is not directed to children under 13 and we do not
      knowingly collect personal information from them.
    </p>
  </div>

  <div>
    <h2 class="font-display text-2xl text-ink-light dark:text-ink-dark mb-3">
      7. Changes
    </h2>
    <p>
      We may update this policy from time to time. The “Last updated”
      date above reflects the most recent revision.
    </p>
  </div>

  <div>
    <h2 class="font-display text-2xl text-ink-light dark:text-ink-dark mb-3">
      8. Contact
    </h2>
    <p>
      Questions? Email
      <a class="underline decoration-accent-500 underline-offset-4" href={`mailto:${contactEmail}`}>{contactEmail}</a>.
    </p>
  </div>
</section>
