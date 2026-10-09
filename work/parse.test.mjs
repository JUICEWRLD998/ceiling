import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import { parseLeaderboard } from './parse.mjs';

test('planted all-100% fraction leaderboard parses with scale fraction and all ones', () => {
  const r = parseLeaderboard('Model,(Overall),t1,t2\nA,1,1,1\nB,1,1,1\nC,1,1,1\n');
  assert.equal(r.ok, true); assert.equal(r.scale, 'fraction');
  assert.ok(r.models.every(m => m.overall === 1));
});
test('planted percent leaderboard is rescaled to fractions', () => {
  const r = parseLeaderboard('Model,(Overall),t1\nA,100,100\nB,40,40\n');
  assert.equal(r.scale, 'percent'); assert.equal(r.models[1].overall, 0.4);
});
test('quoted model names with commas survive', () => {
  const r = parseLeaderboard('Model,(Overall),t1\n"Foo, Bar",0.5,0.5\nB,0.4,0.4\n');
  assert.equal(r.models[0].model, 'Foo, Bar');
});
test('non-numeric overall column is rejected, not silently zeroed', () => {
  const r = parseLeaderboard('Model,(Overall),t1\nA,Pass,Pass\nB,Fail,Fail\n');
  assert.equal(r.ok, false);
});
test('real page read earlier: Two Kinds of False Done, 4 models x 8 tasks, known values', () => {
  const p = 'work/raw/lb/iswt42__two-kinds-of-false-done.csv';
  if (!fs.existsSync(p)) return;
  const r = parseLeaderboard(fs.readFileSync(p, 'utf8'));
  assert.equal(r.models.length, 4); assert.equal(r.taskNames.length, 8);
  assert.equal(r.models[0].model, 'Claude Haiku 4.5');
  assert.ok(Math.abs(r.models[0].overall - 0.9140625) < 1e-9);
  assert.equal(r.models[3].tasks['receipt-triplets-t3-do-bare'], 0);
});
