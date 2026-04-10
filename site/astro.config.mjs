import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  site: 'https://j1ngg.github.io',
  base: '/tech-marketing-framework',
  integrations: [tailwind()],
});
