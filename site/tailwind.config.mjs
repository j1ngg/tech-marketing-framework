/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        sage: {
          50: '#f0f5f0',
          100: '#dce8dc',
          200: '#b8d1b8',
          300: '#8fbc8f',
          400: '#6ba86b',
          500: '#4a8a4a',
          600: '#3a6e3a',
          700: '#2d542d',
          800: '#1e3a1e',
          900: '#0f1f0f',
        },
        terminal: '#1e1e2e',
      },
      fontFamily: {
        mono: ['JetBrains Mono', 'Fira Code', 'Courier New', 'monospace'],
      },
    },
  },
  plugins: [],
};
