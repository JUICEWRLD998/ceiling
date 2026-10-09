// Pull every post tagged kagglechallenge, save bodies (git-ignored) and the distinct Kaggle benchmark slugs.
import fs from 'node:fs';
const out = process.argv[2] || '.';
fs.mkdirSync(out + '/raw', { recursive: true });
let list = [];
for (let p = 1; p <= 8; p++) {
  const r = await fetch(`https://dev.to/api/articles?tag=kagglechallenge&per_page=100&page=${p}`);
  const j = await r.json();
  if (!Array.isArray(j) || j.length === 0) break;
  list = list.concat(j);
}
const seen = new Set();
list = list.filter(a => !seen.has(a.id) && seen.add(a.id));
const bodies = {};
for (const a of list) {
  for (let t = 0; t < 3; t++) {
    const r = await fetch(`https://dev.to/api/articles/${a.id}`);
    if (r.ok) { bodies[a.id] = (await r.json()).body_markdown || ''; break; }
    await new Promise(s => setTimeout(s, 1500 * (t + 1)));
  }
  await new Promise(s => setTimeout(s, 200));
}
fs.writeFileSync(out + '/raw/bodies.json', JSON.stringify(bodies));
const stop = new Set([' ', ')', '>', '"', "'", ']', '\n', '\r', '\t', '<', '`']);
function kaggleUrls(text) {
  const urls = [];
  let i = 0;
  while ((i = text.indexOf('kaggle.com/', i)) !== -1) {
    let j = i;
    while (j < text.length && !stop.has(text[j])) j++;
    urls.push(text.slice(i, j).replace(/[.,;:!?*_]+$/, ''));
    i = j;
  }
  return urls;
}
const posts = [];
const slugs = new Map();
for (const a of list) {
  const urls = kaggleUrls(bodies[a.id] || '');
  const mine = new Set();
  for (const u of urls) {
    const parts = u.split(/[?#]/)[0].split('/'); // [kaggle.com, benchmarks, owner, slug, ...]
    if (parts[1] === 'benchmarks' && parts[2] && parts[2] !== 'tasks' && parts[3]) {
      const key = parts[2] + '/' + parts[3];
      mine.add(key);
      if (!slugs.has(key)) slugs.set(key, []);
      slugs.get(key).push(a.id);
    }
  }
  posts.push({ id: a.id, user: a.user.username, title: a.title, url: a.url, reactions: a.public_reactions_count, published: a.published_at, benchmarks: [...mine], kaggleUrls: [...new Set(urls)] });
}
fs.writeFileSync(out + '/../data/posts.json', JSON.stringify(posts, null, 1));
const bench = [...slugs.entries()].map(([slug, ids]) => ({ slug, posts: [...new Set(ids)] }));
fs.writeFileSync(out + '/../data/benchmarks.json', JSON.stringify(bench, null, 1));
console.log('posts', posts.length, 'benchmark slugs', bench.length, 'posts with >=1 slug', posts.filter(p => p.benchmarks.length).length);
