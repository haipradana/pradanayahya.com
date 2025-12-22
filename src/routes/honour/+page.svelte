<script lang="ts">
  import { honours, type HonourType } from '$lib/data/honours';
  import { Briefcase, Trophy, Calendar, GraduationCap } from 'lucide-svelte';

  const typeLabel = (type: HonourType) =>
    type === 'experience' ? 'Experience' : type === 'award' ? 'Award' : 'Education';

  const Icon = (type: HonourType) =>
    type === 'experience' ? Briefcase : type === 'award' ? Trophy : GraduationCap;

  const labelTextClass = (type: HonourType) =>
    type === 'experience'
      ? 'text-sky-700 dark:text-sky-300'
      : type === 'award'
        ? 'text-amber-700 dark:text-amber-300'
        : 'text-violet-700 dark:text-violet-300';

  const honoursNewestFirst = [...honours].reverse();
</script>

<svelte:head>
  <title>Honour - Pradana Yahya</title>
  <meta
    name="description"
    content="Experience & awards timeline of Pradana Yahya."
  />
</svelte:head>

<div class="max-w-5xl mx-auto px-6 lg:px-8 py-12 lg:py-16">
  <section class="text-center mb-10 lg:mb-14">
    <h1 class="text-2xl sm:text-3xl lg:text-4xl font-bold text-gray-900 dark:text-gray-50 mb-3">
      Honour
    </h1>
    <p class="text-sm sm:text-base text-gray-600 dark:text-gray-400 max-w-2xl mx-auto">
      A timeline of experience and awards.
    </p>
  </section>

  <section>
    <div class="relative">
      <!-- Main trunk: left on mobile, center on md+ -->
      <div class="absolute left-4 md:left-1/2 top-0 bottom-0 w-px bg-gray-200 dark:bg-gray-700" />

      <ul class="space-y-10 lg:space-y-12">
        {#each honoursNewestFirst as item, i (item.id)}
          {@const isLeft = i % 2 === 0}
          {@const ItemIcon = Icon(item.type)}

          <li class="relative md:grid md:grid-cols-9 md:gap-x-6">
            <!-- Node + branch -->
            <div class="absolute left-4 md:static md:col-start-5 md:col-span-1 md:flex md:justify-center">
              <div class="relative mt-1 md:mt-6 -translate-x-1/2 md:translate-x-0">
                <div
                  class="relative z-10 flex h-8 w-8 items-center justify-center rounded-full bg-white dark:bg-dark-custom border border-gray-200 dark:border-gray-700 shadow-md"
                >
                  <ItemIcon class="w-4 h-4 text-gray-700 dark:text-gray-200" />
                </div>

                <div
                  class={`hidden md:block absolute top-1/2 -translate-y-1/2 h-px w-10 bg-gray-200 dark:bg-gray-700 ${
                    isLeft ? 'right-full' : 'left-full'
                  }`}
                />
              </div>
            </div>

            <!-- Card -->
            <div
              class={`pl-12 md:pl-0 md:col-span-4 ${
                isLeft ? 'md:col-start-1 md:pr-8 md:text-right' : 'md:col-start-6 md:pl-8'
              }`}
            >
              <article class="card">
                <header class="mb-3">
                  <div class={`flex flex-wrap items-center gap-2 ${isLeft ? 'md:justify-end' : ''}`}>
                    <span class={`px-2 py-1 text-[11px] font-medium rounded-full bg-gray-100 dark:bg-gray-700 ${labelTextClass(item.type)}`}>
                      {typeLabel(item.type)}
                    </span>

                    {#if item.period}
                      <span class="inline-flex items-center text-[11px] text-gray-500 dark:text-gray-400">
                        <Calendar class="w-3 h-3 mr-1" />
                        {item.period.from}
                        {#if item.period.to && item.period.to !== item.period.from}
                          {' → '}
                          {item.period.to}
                        {/if}
                      </span>
                    {/if}
                  </div>

                  <h2 class="text-base sm:text-lg font-semibold text-gray-900 dark:text-gray-100 mt-2">
                    {item.title}
                  </h2>

                  {#if item.org}
                    <p class="text-sm text-gray-600 dark:text-gray-400 mt-1">
                      {item.org}
                    </p>
                  {/if}
                </header>

                {#if item.description}
                  <p class="text-sm text-gray-700 dark:text-gray-300 leading-relaxed">
                    {item.description}
                  </p>
                {/if}

                {#if item.highlights?.length}
                  <ul class={`mt-3 space-y-1 text-sm text-gray-700 dark:text-gray-300 ${isLeft ? 'md:text-right' : ''}`}>
                    {#each item.highlights as h}
                      <li class="leading-relaxed">- {h}</li>
                    {/each}
                  </ul>
                {/if}

                {#if item.tags?.length}
                  <div class={`mt-4 flex flex-wrap gap-2 ${isLeft ? 'md:justify-end' : ''}`}>
                    {#each item.tags as tag}
                      <span class="px-2 py-1 text-[11px] rounded-full bg-gray-50 dark:bg-[#212328] border border-gray-200 dark:border-gray-700 text-gray-600 dark:text-gray-300">
                        {tag}
                      </span>
                    {/each}
                  </div>
                {/if}
              </article>
            </div>
          </li>
        {/each}
      </ul>
    </div>
  </section>
</div>

