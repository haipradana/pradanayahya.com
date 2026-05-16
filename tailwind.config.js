/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  darkMode: 'class',
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        display: ['"Fraunces"', 'Georgia', 'serif'],
        mono: ['"JetBrains Mono"', 'ui-monospace', 'monospace'],
      },
      colors: {
        surface: {
          light: '#faf8f5',
          'light-elev': '#ffffff',
          'light-muted': '#f1ede6',
          dark: '#0c0c0d',
          'dark-elev': '#141416',
          'dark-muted': '#1c1c1f',
        },
        ink: {
          light: '#111111',
          dark: '#f5f5f4',
          'muted-light': '#5a5a5a',
          'muted-dark': '#a1a1aa',
          'faint-light': '#e6e0d6',
          'faint-dark': '#27272a',
        },
        accent: {
          50: '#ecfdf5',
          100: '#d1fae5',
          200: '#a7f3d0',
          300: '#6ee7b7',
          400: '#34d399',
          500: '#10b981',
          600: '#059669',
          700: '#047857',
          800: '#065f46',
          900: '#064e3b',
        },
        'dark-custom': '#0c0c0d',
      },
      backgroundColor: {
        'dark-custom': '#0c0c0d',
      },
      animation: {
        'fade-in': 'fadeIn 0.6s ease-out both',
        'fade-up': 'fadeUp 0.7s cubic-bezier(.2,.7,.2,1) both',
        'slow-pan': 'slowPan 18s ease-in-out infinite alternate',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        fadeUp: {
          '0%': { transform: 'translateY(14px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        slowPan: {
          '0%': { transform: 'scale(1.04) translate3d(0,0,0)' },
          '100%': { transform: 'scale(1.10) translate3d(-2%,-1%,0)' },
        },
      },
    },
  },
  plugins: [],
};
