"""Check built HTML links and fragment targets without requesting external URLs."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
import argparse

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.links, self.ids = [], set()
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if data.get('id'): self.ids.add(data['id'])
        key = 'href' if tag in ('a', 'link') else 'src' if tag in ('script', 'img') else None
        if key and data.get(key): self.links.append(data[key])

def check(directory, base):
    root = Path(directory).resolve()
    if not (root / 'index.html').is_file(): raise SystemExit('Build the site before checking links.')
    base = '/' + base.strip('/') + '/' if base.strip('/') else '/'
    pages = {p:Page(p.read_text()) for p in root.rglob('*.html')}
    errors = []
    for file, page in pages.items():
        relative = file.relative_to(root).as_posix()
        route = base + (relative[:-10] if relative.endswith('index.html') else relative)
        for link in page.links:
            # Cross-site links are verified together in local browser QA.
            if urlsplit(link).scheme or link.startswith('//'): continue
            parsed = urlsplit(urljoin('https://local.test' + route, link))
            path = unquote(parsed.path)
            if not path.startswith(base):
                errors.append(f'{relative}: link escapes site base: {link}')
                continue
            target = root / path[len(base):]
            if target.is_dir(): target = target / 'index.html'
            if not target.is_file():
                errors.append(f'{relative}: missing target: {link}')
            elif parsed.fragment and target.suffix == '.html':
                target_page = pages.get(target) or Page(target.read_text())
                if unquote(parsed.fragment) not in target_page.ids:
                    errors.append(f'{relative}: missing fragment: {link}')
    if errors: raise SystemExit('\n'.join(errors))
    print(f'Checked {len(pages)} HTML pages: internal links, assets and fragment targets are valid.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', nargs='?', default='dist')
    parser.add_argument('--base', default='/')
    args = parser.parse_args()
    check(args.directory, args.base)
