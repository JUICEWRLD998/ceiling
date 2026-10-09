# Decisions (newest first)

## 2026-10-09 Branch A confirmed (decisive question)
Rule, written before computing: ceiling = rank-1 to rank-3 overall gap <= D points AND top overall >= 0.90.
Result on 71 benchmarks with 3+ models (of 90 parsed, 99 linked): ceiling share 47.9% at D=2, 49.3% at D=3, 54.9% at D=5.
Median top overall score = 1.00. Median rank1-to-rank3 gap = 1.2 points.
Caveats to state in the post: rosters differ per benchmark; 19 benchmarks had under 3 models; 9 benchmarks unparsed or private;
33 posts link only task pages, not benchmark pages; some benchmarks are regression checks by design.
Evidence: data/summary.json, data/audit.json, work/metrics.mjs. Rejected alternative: Branch B (topic families first), not needed.
