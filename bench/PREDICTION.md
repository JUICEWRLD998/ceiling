# Sealed prediction for Ladder (written 2026-10-09, before any model has seen an item)

Benchmark: 90 generated state-tracking items (ledger, queue, strings) on six rungs of k = 3, 6, 10, 15, 22, 30 operations.
Scoring: exact match on the last ANSWER line. No LLM judge.

1. On rung k=3 and k=6 the top-3 models are within 3 points of each other and at or above 0.90 (the audit's ceiling rule fires).
2. On rung k=22 and k=30 the rank-1 to rank-3 gap is at least 10 points (the ceiling rule does not fire).
3. Overall (mean of six rungs) the rank-1 to rank-3 gap is at least 5 points, so Ladder passes the same test I apply to the cohort.
4. Reasoning-enabled models beat their non-reasoning siblings on k >= 15 by at least 15 points.
5. Small models (nano, flash-lite, mini, 4B-31B open weights) reach 0.5 or below on k = 30.
6. The ledger family is easiest and the strings family hardest at k >= 15.

If 1 or 3 fails, Ladder also saturates and the post says so.
