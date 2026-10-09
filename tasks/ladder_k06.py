# %%
import kaggle_benchmarks as kbench
import pandas as pd

# Ladder, rung k=6: 15 generated state-tracking items (ledger, queue, strings), exact-match scoring, no LLM judge.
# Generator and tests: https://github.com/JUICEWRLD998/ceiling (bench/ladder_gen.py)
ROWS = [
 {
  "id": "ledger-k06-s11",
  "prompt": "Accounts A, B, C start with A=30, B=87, C=80. Apply the steps in order. If the source account holds less than the amount, that step does nothing.\n\n1. Move 35 from B to C.\n2. Move 29 from A to C.\n3. Move 5 from A to B.\n4. Move 45 from B to A.\n5. Move 45 from A to C.\n6. Move 60 from B to A.\n\nGive the final balances as A=..,B=..,C=... End your reply with one line: ANSWER: <final answer>",
  "answer": "A=1,B=7,C=189"
 },
 {
  "id": "ledger-k06-s23",
  "prompt": "Accounts A, B, C start with A=51, B=56, C=44. Apply the steps in order. If the source account holds less than the amount, that step does nothing.\n\n1. Move 49 from C to A.\n2. Move 12 from A to B.\n3. Move 27 from C to B.\n4. Move 47 from A to C.\n5. Move 27 from A to C.\n6. Move 11 from B to C.\n\nGive the final balances as A=..,B=..,C=... End your reply with one line: ANSWER: <final answer>",
  "answer": "A=12,B=84,C=55"
 },
 {
  "id": "ledger-k06-s37",
  "prompt": "Accounts A, B, C start with A=68, B=90, C=70. Apply the steps in order. If the source account holds less than the amount, that step does nothing.\n\n1. Move 5 from C to A.\n2. Move 10 from A to B.\n3. Move 12 from B to C.\n4. Move 7 from A to B.\n5. Move 44 from C to A.\n6. Move 7 from C to A.\n\nGive the final balances as A=..,B=..,C=... End your reply with one line: ANSWER: <final answer>",
  "answer": "A=107,B=95,C=26"
 },
 {
  "id": "ledger-k06-s41",
  "prompt": "Accounts A, B, C start with A=40, B=26, C=85. Apply the steps in order. If the source account holds less than the amount, that step does nothing.\n\n1. Move 40 from C to A.\n2. Move 33 from C to A.\n3. Move 14 from C to B.\n4. Move 33 from C to A.\n5. Move 10 from C to B.\n6. Move 5 from C to A.\n\nGive the final balances as A=..,B=..,C=... End your reply with one line: ANSWER: <final answer>",
  "answer": "A=113,B=36,C=2"
 },
 {
  "id": "ledger-k06-s59",
  "prompt": "Accounts A, B, C start with A=76, B=44, C=84. Apply the steps in order. If the source account holds less than the amount, that step does nothing.\n\n1. Move 5 from B to C.\n2. Move 47 from B to C.\n3. Move 53 from A to B.\n4. Move 39 from B to A.\n5. Move 36 from B to A.\n6. Move 7 from B to A.\n\nGive the final balances as A=..,B=..,C=... End your reply with one line: ANSWER: <final answer>",
  "answer": "A=105,B=10,C=89"
 },
 {
  "id": "queue-k06-s11",
  "prompt": "A list starts as [V,T,Z,W,U]. Apply the steps in order.\n\n1. Rotate left by 4.\n2. Swap positions 1 and 5 (1-based).\n3. Reverse the list.\n4. Append g at the end.\n5. Rotate left by 3.\n6. Rotate left by 4.\n\nGive the final list as comma-separated items, or EMPTY. End your reply with one line: ANSWER: <final answer>",
  "answer": "Z,T,V,W,g,U"
 },
 {
  "id": "queue-k06-s23",
  "prompt": "A list starts as [Q,W,U,T,S]. Apply the steps in order.\n\n1. Remove the first item.\n2. Rotate left by 4.\n3. Append b at the end.\n4. Append g at the end.\n5. Reverse the list.\n6. Append h at the end.\n\nGive the final list as comma-separated items, or EMPTY. End your reply with one line: ANSWER: <final answer>",
  "answer": "g,b,S,T,U,W,h"
 },
 {
  "id": "queue-k06-s37",
  "prompt": "A list starts as [T,S,Q,W,R]. Apply the steps in order.\n\n1. Rotate left by 1.\n2. Reverse the list.\n3. Reverse the list.\n4. Append b at the end.\n5. Rotate left by 4.\n6. Append g at the end.\n\nGive the final list as comma-separated items, or EMPTY. End your reply with one line: ANSWER: <final answer>",
  "answer": "T,b,S,Q,W,R,g"
 },
 {
  "id": "queue-k06-s41",
  "prompt": "A list starts as [Y,Q,V,U,X]. Apply the steps in order.\n\n1. Remove the first item.\n2. Append h at the end.\n3. Swap positions 4 and 2 (1-based).\n4. Swap positions 1 and 4 (1-based).\n5. Reverse the list.\n6. Swap positions 2 and 5 (1-based).\n\nGive the final list as comma-separated items, or EMPTY. End your reply with one line: ANSWER: <final answer>",
  "answer": "h,V,U,X,Q"
 },
 {
  "id": "queue-k06-s59",
  "prompt": "A list starts as [W,Q,U,X,R]. Apply the steps in order.\n\n1. Remove the first item.\n2. Append d at the end.\n3. Append h at the end.\n4. Reverse the list.\n5. Remove the first item.\n6. Swap positions 5 and 1 (1-based).\n\nGive the final list as comma-separated items, or EMPTY. End your reply with one line: ANSWER: <final answer>",
  "answer": "Q,R,X,U,d"
 },
 {
  "id": "strings-k06-s11",
  "prompt": "A string starts as 'adabddcbc'. Apply the steps in order. If the letter is absent, the step does nothing.\n\n1. Replace the first 'a' with 'b'.\n2. Replace the first 'd' with 'd'.\n3. Replace the first 'b' with 'd'.\n4. Replace the first 'c' with 'd'.\n5. Replace the first 'd' with 'd'.\n6. Replace the first 'b' with 'a'.\n\nGive the final string. End your reply with one line: ANSWER: <final answer>",
  "answer": "ddaadddbc"
 },
 {
  "id": "strings-k06-s23",
  "prompt": "A string starts as 'ddcdbcabd'. Apply the steps in order. If the letter is absent, the step does nothing.\n\n1. Replace the first 'd' with 'c'.\n2. Replace the first 'b' with 'c'.\n3. Replace the first 'b' with 'a'.\n4. Replace the first 'd' with 'a'.\n5. Replace the first 'a' with 'b'.\n6. Replace the first 'd' with 'c'.\n\nGive the final string. End your reply with one line: ANSWER: <final answer>",
  "answer": "cbccccaad"
 },
 {
  "id": "strings-k06-s37",
  "prompt": "A string starts as 'cabbcbdca'. Apply the steps in order. If the letter is absent, the step does nothing.\n\n1. Replace the first 'b' with 'd'.\n2. Replace the first 'c' with 'c'.\n3. Replace the first 'b' with 'c'.\n4. Replace the first 'a' with 'c'.\n5. Replace the first 'a' with 'a'.\n6. Replace the first 'd' with 'd'.\n\nGive the final string. End your reply with one line: ANSWER: <final answer>",
  "answer": "ccdccbdca"
 },
 {
  "id": "strings-k06-s41",
  "prompt": "A string starts as 'adbadbdad'. Apply the steps in order. If the letter is absent, the step does nothing.\n\n1. Replace the first 'd' with 'b'.\n2. Replace the first 'b' with 'b'.\n3. Replace the first 'a' with 'c'.\n4. Replace the first 'b' with 'b'.\n5. Replace the first 'b' with 'c'.\n6. Replace the first 'a' with 'a'.\n\nGive the final string. End your reply with one line: ANSWER: <final answer>",
  "answer": "ccbadbdad"
 },
 {
  "id": "strings-k06-s59",
  "prompt": "A string starts as 'dadbbdccc'. Apply the steps in order. If the letter is absent, the step does nothing.\n\n1. Replace the first 'a' with 'a'.\n2. Replace the first 'a' with 'b'.\n3. Replace the first 'd' with 'c'.\n4. Replace the first 'd' with 'a'.\n5. Replace the first 'b' with 'b'.\n6. Replace the first 'd' with 'd'.\n\nGive the final string. End your reply with one line: ANSWER: <final answer>",
  "answer": "cbabbdccc"
 }
]


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
@kbench.task(name="ladder-item-k06", store_task=False)
def ladder_item_k06(llm, prompt: str, answer: str) -> bool:
    out = llm.prompt(prompt)
    return _norm(_extract(out)) == _norm(answer)


# %%
@kbench.task(name="ladder-k06")
def ladder_k06(llm) -> float:
    df = pd.DataFrame(ROWS)
    results = ladder_item_k06.evaluate(llm=[llm], evaluation_data=df[["prompt", "answer"]], n_jobs=8, on_failure="continue", max_attempts=2)
    scores = results.completed_runs.as_dataframe().result
    return float(scores.mean())


ladder_k06.run(kbench.llm)
