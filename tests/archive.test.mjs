import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';

function body(path) {
  return readFileSync(new URL(path, import.meta.url), 'utf8')
    .replace(/^---\r?\n[\s\S]*?\r?\n---\r?\n/, '')
    .trim();
}
test('all three migrated notes preserve the original bodies', () => {
  const pairs = [
    ['git-notes', '2025/202512/2025-12-25-coding-part.md'],
    ['frontend-backend', '2025/202512/2025-12-26_coding-part.md'],
    ['battle-game', 'project/battlegame_projnote.md'],
  ];
  for (const [id, path] of pairs)
    assert.equal(
      body(`../src/content/archive/${id}.md`),
      body(`../_posts/${path}`),
      id,
    );
});
