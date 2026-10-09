# %%
import kaggle_benchmarks as kbench
import pandas as pd

# Ladder, rung k=10: 15 generated state-tracking items (ledger, queue, strings), exact-match scoring, no LLM judge.
# Generator and tests: https://github.com/JUICEWRLD998/ceiling (bench/ladder_gen.py)
ROWS = [
 {
  "id": "ledger-k10-s11",
  "prompt": "Accounts A, B, C start with A=62, B=57, C=89. Apply the steps in order. If the source account holds less than the amount, that step does nothing.\n\n1. Move 32 from C to A.\n2. Move 7 from A to C.\n3. Move 54 from B to C.\n4. Move 8 from A to B.\n5. Move 60 from B to C.\n6. Move 27 from A to C.\n7. Move 34 from B to A.\n8. Move 28 from C to A.\n9. Move 31 from C to A.\n10. Move 56 from C to B.\n\nGive the final balances as A=..,B=..,C=... End your reply with one line: ANSWER: <final answer>",
  "answer": "A=111,B=67,C=30"
 },
 {
  "id": "ledger-k10-s23",
  "prompt": "Accounts A, B, C start with A=81, B=80, C=32. Apply the steps in order. If the source account holds less than the amount, that step does nothing.\n\n1. Move 50 from C to B.\n2. Move 57 from B to C.\n3. Move 39 from B to A.\n4. Move 47 from A to C.\n5. Move 34 from C to A.\n6. Move 37 from C to B.\n7. Move 59 from B to C.\n8. Move 45 from A to C.\n9. Move 8 from B to A.\n10. Move 57 from B to A.\n\nGive the final balances as A=..,B=..,C=... End your reply with one line: ANSWER: <final answer>",
  "answer": "A=23,B=1,C=169"
 },
 {
  "id": "ledger-k10-s37",
  "prompt": "Accounts A, B, C start with A=63, B=58, C=22. Apply the steps in order. If the source account holds less than the amount, that step does nothing.\n\n1. Move 24 from B to C.\n2. Move 23 from A to C.\n3. Move 53 from B to C.\n4. Move 22 from A to B.\n5. Move 29 from B to A.\n6. Move 59 from C to B.\n7. Move 47 from B to C.\n8. Move 28 from B to C.\n9. Move 29 from C to A.\n10. Move 10 from C to B.\n\nGive the final balances as A=..,B=..,C=... End your reply with one line: ANSWER: <final answer>",
  "answer": "A=76,B=21,C=46"
 },
 {
  "id": "ledger-k10-s41",
  "prompt": "Accounts A, B, C start with A=67, B=83, C=48. Apply the steps in order. If the source account holds less than the amount, that step does nothing.\n\n1. Move 14 from B to A.\n2. Move 21 from B to A.\n3. Move 43 from C to B.\n4. Move 32 from B to C.\n5. Move 15 from A to C.\n6. Move 46 from C to A.\n7. Move 54 from A to B.\n8. Move 28 from C to A.\n9. Move 50 from C to A.\n10. Move 8 from B to A.\n\nGive the final balances as A=..,B=..,C=... End your reply with one line: ANSWER: <final answer>",
  "answer": "A=87,B=105,C=6"
 },
 {
  "id": "ledger-k10-s59",
  "prompt": "Accounts A, B, C start with A=57, B=42, C=22. Apply the steps in order. If the source account holds less than the amount, that step does nothing.\n\n1. Move 46 from B to A.\n2. Move 15 from C to B.\n3. Move 44 from B to A.\n4. Move 29 from A to B.\n5. Move 13 from C to A.\n6. Move 50 from C to B.\n7. Move 57 from A to C.\n8. Move 59 from B to C.\n9. Move 55 from A to C.\n10. Move 9 from B to C.\n\nGive the final balances as A=..,B=..,C=... End your reply with one line: ANSWER: <final answer>",
  "answer": "A=15,B=33,C=73"
 },
 {
  "id": "queue-k10-s11",
  "prompt": "A list starts as [W,V,T,Z,R]. Apply the steps in order.\n\n1. Rotate left by 2.\n2. Remove the first item.\n3. Append d at the end.\n4. Swap positions 4 and 5 (1-based).\n5. Reverse the list.\n6. Append e at the end.\n7. Remove the first item.\n8. Remove the first item.\n9. Rotate left by 3.\n10. Swap positions 3 and 1 (1-based).\n\nGive the final list as comma-separated items, or EMPTY. End your reply with one line: ANSWER: <final answer>",
  "answer": "R,W,e,Z"
 },
 {
  "id": "queue-k10-s23",
  "prompt": "A list starts as [S,X,Y,P,Z]. Apply the steps in order.\n\n1. Swap positions 1 and 4 (1-based).\n2. Append e at the end.\n3. Reverse the list.\n4. Reverse the list.\n5. Remove the first item.\n6. Swap positions 2 and 5 (1-based).\n7. Remove the first item.\n8. Remove the first item.\n9. Reverse the list.\n10. Reverse the list.\n\nGive the final list as comma-separated items, or EMPTY. End your reply with one line: ANSWER: <final answer>",
  "answer": "S,Z,Y"
 },
 {
  "id": "queue-k10-s37",
  "prompt": "A list starts as [Z,Q,S,T,V]. Apply the steps in order.\n\n1. Remove the first item.\n2. Swap positions 3 and 1 (1-based).\n3. Swap positions 4 and 3 (1-based).\n4. Remove the first item.\n5. Reverse the list.\n6. Rotate left by 3.\n7. Rotate left by 2.\n8. Remove the first item.\n9. Append a at the end.\n10. Append a at the end.\n\nGive the final list as comma-separated items, or EMPTY. End your reply with one line: ANSWER: <final answer>",
  "answer": "Q,V,a,a"
 },
 {
  "id": "queue-k10-s41",
  "prompt": "A list starts as [T,V,S,X,P]. Apply the steps in order.\n\n1. Reverse the list.\n2. Append a at the end.\n3. Remove the first item.\n4. Remove the first item.\n5. Swap positions 4 and 2 (1-based).\n6. Reverse the list.\n7. Swap positions 2 and 3 (1-based).\n8. Remove the first item.\n9. Remove the first item.\n10. Rotate left by 2.\n\nGive the final list as comma-separated items, or EMPTY. End your reply with one line: ANSWER: <final answer>",
  "answer": "T,S"
 },
 {
  "id": "queue-k10-s59",
  "prompt": "A list starts as [Q,U,R,S,W]. Apply the steps in order.\n\n1. Swap positions 5 and 3 (1-based).\n2. Rotate left by 3.\n3. Swap positions 3 and 4 (1-based).\n4. Rotate left by 2.\n5. Rotate left by 1.\n6. Append c at the end.\n7. Swap positions 3 and 5 (1-based).\n8. Append d at the end.\n9. Append e at the end.\n10. Remove the first item.\n\nGive the final list as comma-separated items, or EMPTY. End your reply with one line: ANSWER: <final answer>",
  "answer": "W,U,R,S,c,d,e"
 },
 {
  "id": "strings-k10-s11",
  "prompt": "A string starts as 'bacabbaad'. Apply the steps in order. If the letter is absent, the step does nothing.\n\n1. Replace the first 'c' with 'a'.\n2. Replace the first 'c' with 'a'.\n3. Replace the first 'c' with 'd'.\n4. Replace the first 'c' with 'b'.\n5. Replace the first 'b' with 'd'.\n6. Replace the first 'd' with 'b'.\n7. Replace the first 'b' with 'b'.\n8. Replace the first 'b' with 'd'.\n9. Replace the first 'b' with 'a'.\n10. Replace the first 'b' with 'b'.\n\nGive the final string. End your reply with one line: ANSWER: <final answer>",
  "answer": "daaaabaad"
 },
 {
  "id": "strings-k10-s23",
  "prompt": "A string starts as 'dccdbbadc'. Apply the steps in order. If the letter is absent, the step does nothing.\n\n1. Replace the first 'c' with 'b'.\n2. Replace the first 'a' with 'd'.\n3. Replace the first 'd' with 'd'.\n4. Replace the first 'c' with 'a'.\n5. Replace the first 'c' with 'd'.\n6. Replace the first 'a' with 'b'.\n7. Replace the first 'd' with 'd'.\n8. Replace the first 'c' with 'a'.\n9. Replace the first 'b' with 'c'.\n10. Replace the first 'b' with 'c'.\n\nGive the final string. End your reply with one line: ANSWER: <final answer>",
  "answer": "dccdbbddd"
 },
 {
  "id": "strings-k10-s37",
  "prompt": "A string starts as 'bbacccccd'. Apply the steps in order. If the letter is absent, the step does nothing.\n\n1. Replace the first 'd' with 'a'.\n2. Replace the first 'd' with 'd'.\n3. Replace the first 'a' with 'b'.\n4. Replace the first 'a' with 'c'.\n5. Replace the first 'a' with 'd'.\n6. Replace the first 'c' with 'a'.\n7. Replace the first 'a' with 'b'.\n8. Replace the first 'a' with 'd'.\n9. Replace the first 'a' with 'a'.\n10. Replace the first 'a' with 'c'.\n\nGive the final string. End your reply with one line: ANSWER: <final answer>",
  "answer": "bbbbccccc"
 },
 {
  "id": "strings-k10-s41",
  "prompt": "A string starts as 'bcacaccdc'. Apply the steps in order. If the letter is absent, the step does nothing.\n\n1. Replace the first 'd' with 'a'.\n2. Replace the first 'd' with 'a'.\n3. Replace the first 'd' with 'c'.\n4. Replace the first 'c' with 'c'.\n5. Replace the first 'd' with 'a'.\n6. Replace the first 'b' with 'c'.\n7. Replace the first 'b' with 'c'.\n8. Replace the first 'c' with 'b'.\n9. Replace the first 'a' with 'b'.\n10. Replace the first 'b' with 'd'.\n\nGive the final string. End your reply with one line: ANSWER: <final answer>",
  "answer": "dcbcaccac"
 },
 {
  "id": "strings-k10-s59",
  "prompt": "A string starts as 'badaabbcd'. Apply the steps in order. If the letter is absent, the step does nothing.\n\n1. Replace the first 'b' with 'a'.\n2. Replace the first 'c' with 'b'.\n3. Replace the first 'd' with 'a'.\n4. Replace the first 'c' with 'd'.\n5. Replace the first 'a' with 'b'.\n6. Replace the first 'a' with 'c'.\n7. Replace the first 'c' with 'a'.\n8. Replace the first 'd' with 'a'.\n9. Replace the first 'd' with 'b'.\n10. Replace the first 'd' with 'b'.\n\nGive the final string. End your reply with one line: ANSWER: <final answer>",
  "answer": "baaaabbba"
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
@kbench.task(name="ladder-item-k10", store_task=False)
def ladder_item_k10(llm, prompt: str, answer: str) -> bool:
    out = llm.prompt(prompt)
    return _norm(_extract(out)) == _norm(answer)


# %%
@kbench.task(name="ladder-k10")
def ladder_k10(llm) -> float:
    df = pd.DataFrame(ROWS)
    results = ladder_item_k10.evaluate(llm=[llm], evaluation_data=df[["prompt", "answer"]], n_jobs=8, on_failure="continue", max_attempts=2)
    scores = results.completed_runs.as_dataframe().result
    return float(scores.mean())


ladder_k10.run(kbench.llm)
