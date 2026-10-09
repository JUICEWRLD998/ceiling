# Phase 0 notes (2026-10-09)

- 0.4 VERIFIED: `kaggle b leaderboard <owner>/<slug> --download -p <dir>` returns CSV for another user's public benchmark
  (iswt42/two-kinds-of-false-done: Model, (Overall), one column per task, values 0-1). No page scraping needed.
- 0.3 VERIFIED (web UI, user paste): Daily AI Models $10.00, Monthly $100.00, none used.
- `kaggle b auth` returns 403 after phone verification and forced re-login. `kaggle b quota` absent in CLI 2.2.4.
- 0.5 (kaggle-skills write-kaggle-benchmarks SKILL.md): tasks need `.run(kbench.llm)` at the end or they silently no-op;
  the CLI creates TASKS only; a BENCHMARK (collection of tasks) must be created in the Kaggle web UI. The DEV rules want a
  benchmark link, so the own benchmark must be assembled in the web UI from published tasks.
