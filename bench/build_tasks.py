"""Write one self-contained Kaggle task file per Ladder rung into tasks/. Rows are embedded so the task needs no dataset."""
import json
import os
import ladder_gen as g

HEADER = '''# %%
import kaggle_benchmarks as kbench
import pandas as pd

# Ladder, rung k={k}: {n} generated state-tracking items (ledger, queue, strings), exact-match scoring, no LLM judge.
# Generator and tests: https://github.com/JUICEWRLD998/ceiling (bench/ladder_gen.py)
ROWS = {rows}


def _extract(text):
    last = None
    for line in text.splitlines():
        t = line.strip().strip("*`").strip()
        if t.upper().startswith("ANSWER:"):
            last = t[7:].strip().strip("*`").strip()
    return last


def _norm(s):
    return None if s is None else s.replace(" ", "").replace("'", "").replace("[", "").replace("]", "").lower()


# %%
@kbench.task(name="ladder-item-k{k:02d}", store_task=False)
def ladder_item_k{k:02d}(llm, prompt: str, answer: str) -> bool:
    out = llm.prompt(prompt)
    return _norm(_extract(out)) == _norm(answer)


# %%
@kbench.task(name="ladder-k{k:02d}")
def ladder_k{k:02d}(llm) -> float:
    df = pd.DataFrame(ROWS)
    results = ladder_item_k{k:02d}.evaluate(llm=[llm], evaluation_data=df[["prompt", "answer"]], n_jobs=8, on_failure="continue", max_attempts=2)
    scores = results.completed_runs.as_dataframe().result
    return float(scores.mean())


ladder_k{k:02d}.run(kbench.llm)
'''

if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(here, "..", "tasks")
    os.makedirs(out, exist_ok=True)
    for k, items in g.build().items():
        rows = [{"id": i["id"], "prompt": i["prompt"], "answer": i["answer"]} for i in items]
        text = HEADER.format(k=k, n=len(rows), rows=json.dumps(rows, indent=1))
        with open(os.path.join(out, f"ladder_k{k:02d}.py"), "w", newline="\n") as f:
            f.write(text)
        print("wrote", k, len(text))
