// Download every benchmark leaderboard CSV via the Kaggle CLI. Idempotent: skips existing files.
import fs from 'node:fs';
import { spawnSync } from 'node:child_process';
const bench = JSON.parse(fs.readFileSync('data/benchmarks.json', 'utf8'));
fs.mkdirSync('work/raw/lb', { recursive: true });
const status = {};
for (const b of bench) {
  const file = 'work/raw/lb/' + b.slug.replace('/', '__') + '.csv';
  if (fs.existsSync(file)) { status[b.slug] = 'cached'; continue; }
  const tmp = 'work/raw/tmp_' + process.pid;
  fs.mkdirSync(tmp, { recursive: true });
  const r = spawnSync('kaggle', ['b', 'leaderboard', b.slug, '--download', '-p', tmp], { encoding: 'utf8', env: { ...process.env, PYTHONUTF8: '1' }, shell: true });
  const got = fs.readdirSync(tmp).find(f => f.endsWith('.csv'));
  if (got) { fs.renameSync(tmp + '/' + got, file); status[b.slug] = 'ok'; }
  else status[b.slug] = 'fail: ' + ((r.stderr || '') + (r.stdout || '')).trim().split('\n').pop().slice(0, 160);
  fs.rmSync(tmp, { recursive: true, force: true });
  await new Promise(s => setTimeout(s, 700));
}
fs.writeFileSync('data/lb_status.json', JSON.stringify(status, null, 1));
const c = {};
for (const v of Object.values(status)) { const k = v.split(':')[0]; c[k] = (c[k] || 0) + 1; }
console.log(c);
