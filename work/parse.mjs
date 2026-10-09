// Parse Kaggle leaderboard CSVs into score rows. Scale rule: all numeric cells <= 1.0 => fraction; max in (1, 100] => percent.
import fs from 'node:fs';

export function splitCsv(text) {
  const rows = []; let row = []; let cell = ''; let q = false;
  for (let i = 0; i < text.length; i++) {
    const c = text[i];
    if (q) { if (c === '"') { if (text[i + 1] === '"') { cell += '"'; i++; } else q = false; } else cell += c; }
    else if (c === '"') q = true;
    else if (c === ',') { row.push(cell); cell = ''; }
    else if (c === '\n') { row.push(cell.replace(/\r$/, '')); rows.push(row); row = []; cell = ''; }
    else cell += c;
  }
  if (cell.length || row.length) { row.push(cell.replace(/\r$/, '')); rows.push(row); }
  return rows.filter(r => r.length > 1 || (r[0] || '').trim() !== '');
}

export function parseLeaderboard(text) {
  const rows = splitCsv(text);
  if (rows.length < 2) return { ok: false, reason: 'empty' };
  const head = rows[0];
  const body = rows.slice(1);
  const num = v => (v !== '' && v != null && isFinite(Number(v)) ? Number(v) : null);
  const taskCols = [];
  for (let j = 2; j < head.length; j++) {
    const vals = body.map(r => num(r[j]));
    if (vals.filter(v => v !== null).length >= Math.ceil(body.length / 2)) taskCols.push(j);
  }
  const overall = body.map(r => num(r[1]));
  const haveOverall = overall.filter(v => v !== null).length >= Math.ceil(body.length / 2);
  if (!haveOverall) return { ok: false, reason: 'non-numeric overall (' + head[1] + ')' };
  let max = 0;
  for (const v of overall) if (v !== null && v > max) max = v;
  for (const j of taskCols) for (const r of body) { const v = num(r[j]); if (v !== null && v > max) max = v; }
  let scale;
  if (max <= 1.0000001) scale = 'fraction';
  else if (max <= 100.0000001) scale = 'percent';
  else return { ok: false, reason: 'other scale (max ' + max + ')' };
  const div = scale === 'percent' ? 100 : 1;
  const models = body.map((r, i) => ({
    model: r[0],
    overall: overall[i] === null ? null : overall[i] / div,
    tasks: Object.fromEntries(taskCols.map(j => [head[j], num(r[j]) === null ? null : num(r[j]) / div])),
  }));
  return { ok: true, scale, models, taskNames: taskCols.map(j => head[j]) };
}

if (process.argv[1] && process.argv[1].endsWith('parse.mjs') && process.argv[2] === 'run') {
  const dir = 'work/raw/lb';
  const out = {}; const fails = {};
  for (const f of fs.readdirSync(dir).filter(f => f.endsWith('.csv'))) {
    const slug = f.replace('__', '/').replace('.csv', '');
    const res = parseLeaderboard(fs.readFileSync(dir + '/' + f, 'utf8'));
    if (res.ok) out[slug] = res; else fails[slug] = res.reason;
  }
  fs.writeFileSync('data/scores.json', JSON.stringify(out));
  fs.writeFileSync('data/parse_fails.json', JSON.stringify(fails, null, 1));
  console.log('parsed', Object.keys(out).length, 'failed', Object.keys(fails).length);
  for (const [k, v] of Object.entries(fails)) console.log(' -', k, v);
}
