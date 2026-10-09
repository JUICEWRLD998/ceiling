// Per-benchmark ceiling metrics. Rule fixed BEFORE looking: ceiling = top-3 overall within D points AND top overall >= 0.90.
import fs from 'node:fs';
const s = JSON.parse(fs.readFileSync('data/scores.json', 'utf8'));
const rows = [];
for (const [slug, b] of Object.entries(s)) {
  const ov = b.models.map(m => m.overall).filter(v => v !== null).sort((a, c) => c - a);
  if (ov.length < 3) { rows.push({ slug, n: ov.length, skipped: 'fewer than 3 models' }); continue; }
  const gap13 = ov[0] - ov[2];
  const allTop = b.taskNames.filter(t => b.models.every(m => m.tasks[t] === null || m.tasks[t] >= 0.9999)).length;
  rows.push({ slug, n: ov.length, tasks: b.taskNames.length, top: ov[0], gap13, spreadAll: ov[0] - ov[ov.length - 1], tasksAllPerfect: allTop,
    ceil2: gap13 <= 0.02 && ov[0] >= 0.9, ceil3: gap13 <= 0.03 && ov[0] >= 0.9, ceil5: gap13 <= 0.05 && ov[0] >= 0.9 });
}
const ok = rows.filter(r => !r.skipped);
const share = k => (ok.filter(r => r[k]).length / ok.length);
const med = a => { const x = a.slice().sort((p, q) => p - q); return x[Math.floor(x.length / 2)]; };
const sum = { benchmarks_parsed: rows.length, with_3plus_models: ok.length, skipped: rows.length - ok.length,
  ceiling_share_2pts: share('ceil2'), ceiling_share_3pts: share('ceil3'), ceiling_share_5pts: share('ceil5'),
  median_top: med(ok.map(r => r.top)), median_gap_rank1_to_3: med(ok.map(r => r.gap13)),
  share_top_ge_90: ok.filter(r => r.top >= 0.9).length / ok.length,
  share_with_a_perfect_for_all_models_task: ok.filter(r => r.tasksAllPerfect > 0).length / ok.length };
fs.writeFileSync('data/audit.json', JSON.stringify(rows, null, 1));
fs.writeFileSync('data/summary.json', JSON.stringify(sum, null, 1));
console.log(sum);
