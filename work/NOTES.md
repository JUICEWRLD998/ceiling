# Phase 0 notes (2026-10-09)

- 0.4 VERIFIED: `kaggle b leaderboard <owner>/<slug> --download -p <dir>` returns CSV for another user's public benchmark
  (iswt42/two-kinds-of-false-done: Model, (Overall), one column per task, values 0-1). No page scraping needed.
- 0.3 VERIFIED (web UI, user paste): Daily AI Models $10.00, Monthly $100.00, none used.
- `kaggle b auth` returns 403 after phone verification and forced re-login. `kaggle b quota` absent in CLI 2.2.4.
- 0.5 (kaggle-skills write-kaggle-benchmarks SKILL.md): tasks need `.run(kbench.llm)` at the end or they silently no-op;
  the CLI creates TASKS only; a BENCHMARK (collection of tasks) must be created in the Kaggle web UI. The DEV rules want a
  benchmark link, so the own benchmark must be assembled in the web UI from published tasks.
- 0.1 FAILED so far: `kaggle b t push` (CLI 2.2.4) prints "An error occurred while saving the entity changes" but tasks DO appear
  in `kaggle b t list` with Status Unspecified; `run` refuses ("not ready, status UNSPECIFIED"). Same account likely lacks
  Model Proxy enablement (b auth 403). Fallback 0.2: build the task in the Kaggle web editor.
- Windows: set PYTHONUTF8=1 or the CLI crashes on table box-drawing chars (charmap error).
- 0.6 DONE: grep of 175 post bodies (other entries|all the benchmarks|this challenge|cohort...) -> 9 hits, all incidental or a link to ONE other entry.
  No cohort-wide audit exists. Empty cell stands (2026-10-09).
- Harvest (work/harvest.mjs): 175 posts, 99 distinct owner/slug benchmark pages; 33 more posts link only /benchmarks/tasks/... pages.
- 1.2 DONE: 99 benchmark slugs -> 93 CSVs downloaded (5 x 403 forbidden, likely private/unpublished; 1 "No results").
- 1.3/1.4 DONE: parser + 5 tests pass (planted ceiling, planted percent, quoted commas, non-numeric overall rejected, real Two Kinds page).
  90 of 99 parsed (91%). 3 rejected for non-numeric overall (Pass/Fail style). Still owed: hand-check 10 pages.
- Gap: 33 posts link only /benchmarks/tasks/... pages (task-level), not benchmark pages. Not covered yet.
