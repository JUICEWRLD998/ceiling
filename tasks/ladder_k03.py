# %%
import kaggle_benchmarks as kbench
import pandas as pd

# Ladder, rung k=3: 15 generated state-tracking items (ledger, queue, strings), exact-match scoring, no LLM judge.
# Generator and tests: https://github.com/JUICEWRLD998/ceiling (bench/ladder_gen.py)
ROWS = [
 {
  "id": "ledger-k03-s11",
  "prompt": "Accounts A, B, C start with A=35, B=57, C=66. Apply the steps in order. If the source account holds less than the amount, that step does nothing.\n\n1. Move 37 from B to C.\n2. Move 52 from B to C.\n3. Move 57 from C to B.\n\nGive the final balances as A=..,B=..,C=... End your reply with one line: ANSWER: <final answer>",
  "answer": "A=35,B=77,C=46"
 },
 {
  "id": "ledger-k03-s23",
  "prompt": "Accounts A, B, C start with A=24, B=36, C=37. Apply the steps in order. If the source account holds less than the amount, that step does nothing.\n\n1. Move 21 from A to C.\n2. Move 25 from A to C.\n3. Move 11 from B to C.\n\nGive the final balances as A=..,B=..,C=... End your reply with one line: ANSWER: <final answer>",
  "answer": "A=3,B=25,C=69"
 },
 {
  "id": "ledger-k03-s37",
  "prompt": "Accounts A, B, C start with A=51, B=23, C=26. Apply the steps in order. If the source account holds less than the amount, that step does nothing.\n\n1. Move 26 from A to C.\n2. Move 18 from C to A.\n3. Move 53 from A to C.\n\nGive the final balances as A=..,B=..,C=... End your reply with one line: ANSWER: <final answer>",
  "answer": "A=43,B=23,C=34"
 },
 {
  "id": "ledger-k03-s41",
  "prompt": "Accounts A, B, C start with A=64, B=68, C=63. Apply the steps in order. If the source account holds less than the amount, that step does nothing.\n\n1. Move 18 from C to A.\n2. Move 11 from C to A.\n3. Move 48 from C to B.\n\nGive the final balances as A=..,B=..,C=... End your reply with one line: ANSWER: <final answer>",
  "answer": "A=93,B=68,C=34"
 },
 {
  "id": "ledger-k03-s59",
  "prompt": "Accounts A, B, C start with A=22, B=88, C=52. Apply the steps in order. If the source account holds less than the amount, that step does nothing.\n\n1. Move 19 from B to A.\n2. Move 55 from B to C.\n3. Move 38 from B to A.\n\nGive the final balances as A=..,B=..,C=... End your reply with one line: ANSWER: <final answer>",
  "answer": "A=41,B=14,C=107"
 },
 {
  "id": "queue-k03-s11",
  "prompt": "A list starts as [X,Y,R,S,V]. Apply the steps in order.\n\n1. Reverse the list.\n2. Rotate left by 3.\n3. Remove the first item.\n\nGive the final list as comma-separated items, or EMPTY. End your reply with one line: ANSWER: <final answer>",
  "answer": "X,V,S,R"
 },
 {
  "id": "queue-k03-s23",
  "prompt": "A list starts as [Q,W,Z,T,R]. Apply the steps in order.\n\n1. Remove the first item.\n2. Append b at the end.\n3. Remove the first item.\n\nGive the final list as comma-separated items, or EMPTY. End your reply with one line: ANSWER: <final answer>",
  "answer": "Z,T,R,b"
 },
 {
  "id": "queue-k03-s37",
  "prompt": "A list starts as [U,W,Z,Y,R]. Apply the steps in order.\n\n1. Swap positions 4 and 5 (1-based).\n2. Reverse the list.\n3. Rotate left by 4.\n\nGive the final list as comma-separated items, or EMPTY. End your reply with one line: ANSWER: <final answer>",
  "answer": "U,Y,R,Z,W"
 },
 {
  "id": "queue-k03-s41",
  "prompt": "A list starts as [V,R,P,U,X]. Apply the steps in order.\n\n1. Append d at the end.\n2. Rotate left by 1.\n3. Remove the first item.\n\nGive the final list as comma-separated items, or EMPTY. End your reply with one line: ANSWER: <final answer>",
  "answer": "P,U,X,d,V"
 },
 {
  "id": "queue-k03-s59",
  "prompt": "A list starts as [U,Y,Q,W,V]. Apply the steps in order.\n\n1. Reverse the list.\n2. Swap positions 2 and 5 (1-based).\n3. Swap positions 5 and 2 (1-based).\n\nGive the final list as comma-separated items, or EMPTY. End your reply with one line: ANSWER: <final answer>",
  "answer": "V,W,Q,Y,U"
 },
 {
  "id": "strings-k03-s11",
  "prompt": "A string starts as 'cccdacdca'. Apply the steps in order. If the letter is absent, the step does nothing.\n\n1. Replace the first 'c' with 'c'.\n2. Replace the first 'c' with 'b'.\n3. Replace the first 'd' with 'c'.\n\nGive the final string. End your reply with one line: ANSWER: <final answer>",
  "answer": "bcccacdca"
 },
 {
  "id": "strings-k03-s23",
  "prompt": "A string starts as 'bcdcbbbad'. Apply the steps in order. If the letter is absent, the step does nothing.\n\n1. Replace the first 'a' with 'c'.\n2. Replace the first 'a' with 'b'.\n3. Replace the first 'b' with 'c'.\n\nGive the final string. End your reply with one line: ANSWER: <final answer>",
  "answer": "ccdcbbbcd"
 },
 {
  "id": "strings-k03-s37",
  "prompt": "A string starts as 'adddbcdac'. Apply the steps in order. If the letter is absent, the step does nothing.\n\n1. Replace the first 'd' with 'b'.\n2. Replace the first 'd' with 'a'.\n3. Replace the first 'c' with 'c'.\n\nGive the final string. End your reply with one line: ANSWER: <final answer>",
  "answer": "abadbcdac"
 },
 {
  "id": "strings-k03-s41",
  "prompt": "A string starts as 'abbcabacd'. Apply the steps in order. If the letter is absent, the step does nothing.\n\n1. Replace the first 'b' with 'a'.\n2. Replace the first 'c' with 'a'.\n3. Replace the first 'b' with 'c'.\n\nGive the final string. End your reply with one line: ANSWER: <final answer>",
  "answer": "aacaabacd"
 },
 {
  "id": "strings-k03-s59",
  "prompt": "A string starts as 'ccccddaaa'. Apply the steps in order. If the letter is absent, the step does nothing.\n\n1. Replace the first 'a' with 'b'.\n2. Replace the first 'b' with 'a'.\n3. Replace the first 'b' with 'a'.\n\nGive the final string. End your reply with one line: ANSWER: <final answer>",
  "answer": "ccccddaaa"
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
@kbench.task(name="ladder-item-k03", store_task=False)
def ladder_item_k03(llm, prompt: str, answer: str) -> bool:
    out = llm.prompt(prompt)
    return _norm(_extract(out)) == _norm(answer)


# %%
@kbench.task(name="ladder-k03")
def ladder_k03(llm) -> float:
    df = pd.DataFrame(ROWS)
    results = ladder_item_k03.evaluate(llm=[llm], evaluation_data=df[["prompt", "answer"]], n_jobs=8, on_failure="continue", max_attempts=2)
    scores = results.completed_runs.as_dataframe().result
    return float(scores.mean())


ladder_k03.run(kbench.llm)
