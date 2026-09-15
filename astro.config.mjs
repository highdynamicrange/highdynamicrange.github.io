import { defineConfig } from 'astro/config';
export default defineConfig({
  site: 'https://highdynamicrange.github.io',
  output: 'static',
  trailingSlash: 'always',
  redirects: {
    '/posts/2025/12/25/coding_part': '/archive/git-notes/',
    '/year-archive': '/archive/',
    '/portfolio': 'https://highdynamicrange.github.io/hdr-lab/projects/',
  },
});
