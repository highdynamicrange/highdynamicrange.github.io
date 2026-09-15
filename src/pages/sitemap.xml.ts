import { getCollection } from 'astro:content';
export async function GET() {
  const paths = [
    '',
    'about/',
    'archive/',
    ...(await getCollection('archive')).map((e) => `archive/${e.id}/`),
  ];
  return new Response(
    `<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">${paths.map((p) => `<url><loc>https://highdynamicrange.github.io/${p}</loc></url>`).join('')}</urlset>`,
    { headers: { 'Content-Type': 'application/xml; charset=utf-8' } },
  );
}
