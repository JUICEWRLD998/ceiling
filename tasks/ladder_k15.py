# %%
import kaggle_benchmarks as kbench
import pandas as pd

# Ladder, rung k=15: 15 generated state-tracking items (ledger, queue, strings), exact-match scoring, no LLM judge.
# Generator and tests: https://github.com/JUICEWRLD998/ceiling (bench/ladder_gen.py)
ROWS = [
 {
  "id": "ledger-k15-s11",
  "prompt": "Accounts A, B, C start with A=54, B=78, C=55. Apply the steps in order. If the source account holds less than the amount, that step does nothing.\n\n1. Move 32 from A to B.\n2. Move 36 from C to A.\n3. Move 25 from A to C.\n4. Move 48 from A to B.\n5. Move 45 from C to A.\n6. Move 50 from C to B.\n7. Move 31 from A to C.\n8. Move 24 from A to C.\n9. Move 27 from C to A.\n10. Move 28 from A to C.\n11. Move 58 from C to A.\n12. Move 52 from A to B.\n13. Move 60 from A to C.\n14. Move 13 from A to B.\n15. Move 23 from A to C.\n\nGive the final balances as A=..,B=..,C=... End your reply with one line: ANSWER: <final answer>",
  "answer": "A=7,B=162,C=18"
 },
 {
  "id": "ledger-k15-s23",
  "prompt": "Accounts A, B, C start with A=46, B=35, C=41. Apply the steps in order. If the source account holds less than the amount, that step does nothing.\n\n1. Move 44 from A to C.\n2. Move 27 from B to C.\n3. Move 23 from A to B.\n4. Move 10 from B to A.\n5. Move 34 from C to A.\n6. Move 7 from C to A.\n7. Move 25 from A to B.\n8. Move 6 from A to C.\n9. Move 37 from A to B.\n10. Move 19 from B to A.\n11. Move 32 from B to C.\n12. Move 32 from A to B.\n13. Move 56 from B to A.\n14. Move 10 from B to C.\n15. Move 19 from B to C.\n\nGive the final balances as A=..,B=..,C=... End your reply with one line: ANSWER: <final answer>",
  "answer": "A=31,B=4,C=87"
 },
 {
  "id": "ledger-k15-s37",
  "prompt": "Accounts A, B, C start with A=26, B=46, C=26. Apply the steps in order. If the source account holds less than the amount, that step does nothing.\n\n1. Move 35 from A to C.\n2. Move 49 from B to C.\n3. Move 55 from A to C.\n4. Move 8 from A to B.\n5. Move 11 from B to A.\n6. Move 47 from C to A.\n7. Move 24 from C to B.\n8. Move 39 from A to C.\n9. Move 10 from C to B.\n10. Move 50 from B to A.\n11. Move 31 from A to C.\n12. Move 40 from A to B.\n13. Move 28 from B to C.\n14. Move 14 from C to B.\n15. Move 6 from B to A.\n\nGive the final balances as A=..,B=..,C=... End your reply with one line: ANSWER: <final answer>",
  "answer": "A=14,B=37,C=47"
 },
 {
  "id": "ledger-k15-s41",
  "prompt": "Accounts A, B, C start with A=37, B=80, C=35. Apply the steps in order. If the source account holds less than the amount, that step does nothing.\n\n1. Move 50 from C to A.\n2. Move 34 from C to B.\n3. Move 14 from A to B.\n4. Move 16 from A to C.\n5. Move 42 from B to C.\n6. Move 15 from A to C.\n7. Move 17 from B to C.\n8. Move 31 from B to A.\n9. Move 57 from A to B.\n10. Move 21 from A to C.\n11. Move 7 from C to B.\n12. Move 32 from C to B.\n13. Move 52 from A to C.\n14. Move 18 from B to C.\n15. Move 41 from B to C.\n\nGive the final balances as A=..,B=..,C=... End your reply with one line: ANSWER: <final answer>",
  "answer": "A=17,B=18,C=117"
 },
 {
  "id": "ledger-k15-s59",
  "prompt": "Accounts A, B, C start with A=74, B=34, C=80. Apply the steps in order. If the source account holds less than the amount, that step does nothing.\n\n1. Move 49 from A to B.\n2. Move 25 from A to C.\n3. Move 15 from C to A.\n4. Move 18 from A to C.\n5. Move 50 from A to B.\n6. Move 10 from B to C.\n7. Move 54 from B to A.\n8. Move 24 from A to B.\n9. Move 44 from C to A.\n10. Move 57 from C to A.\n11. Move 44 from B to A.\n12. Move 8 from A to B.\n13. Move 33 from C to B.\n14. Move 48 from B to A.\n15. Move 58 from C to A.\n\nGive the final balances as A=..,B=..,C=... End your reply with one line: ANSWER: <final answer>",
  "answer": "A=129,B=36,C=23"
 },
 {
  "id": "queue-k15-s11",
  "prompt": "A list starts as [S,Q,Z,U,V]. Apply the steps in order.\n\n1. Rotate left by 3.\n2. Rotate left by 2.\n3. Append f at the end.\n4. Reverse the list.\n5. Rotate left by 4.\n6. Append f at the end.\n7. Remove the first item.\n8. Append g at the end.\n9. Swap positions 4 and 7 (1-based).\n10. Append b at the end.\n11. Append f at the end.\n12. Reverse the list.\n13. Rotate left by 3.\n14. Swap positions 7 and 6 (1-based).\n15. Rotate left by 1.\n\nGive the final list as comma-separated items, or EMPTY. End your reply with one line: ANSWER: <final answer>",
  "answer": "Z,g,V,f,f,S,b,U,f"
 },
 {
  "id": "queue-k15-s23",
  "prompt": "A list starts as [R,U,V,W,T]. Apply the steps in order.\n\n1. Append h at the end.\n2. Remove the first item.\n3. Remove the first item.\n4. Rotate left by 2.\n5. Rotate left by 2.\n6. Reverse the list.\n7. Rotate left by 4.\n8. Append b at the end.\n9. Reverse the list.\n10. Remove the first item.\n11. Reverse the list.\n12. Reverse the list.\n13. Reverse the list.\n14. Rotate left by 4.\n15. Reverse the list.\n\nGive the final list as comma-separated items, or EMPTY. End your reply with one line: ANSWER: <final answer>",
  "answer": "V,W,T,h"
 },
 {
  "id": "queue-k15-s37",
  "prompt": "A list starts as [U,X,Y,Z,T]. Apply the steps in order.\n\n1. Rotate left by 2.\n2. Reverse the list.\n3. Rotate left by 3.\n4. Swap positions 4 and 3 (1-based).\n5. Remove the first item.\n6. Remove the first item.\n7. Rotate left by 1.\n8. Reverse the list.\n9. Append c at the end.\n10. Append a at the end.\n11. Remove the first item.\n12. Reverse the list.\n13. Remove the first item.\n14. Remove the first item.\n15. Reverse the list.\n\nGive the final list as comma-separated items, or EMPTY. End your reply with one line: ANSWER: <final answer>",
  "answer": "T,X"
 },
 {
  "id": "queue-k15-s41",
  "prompt": "A list starts as [X,Q,S,R,W]. Apply the steps in order.\n\n1. Rotate left by 2.\n2. Append e at the end.\n3. Remove the first item.\n4. Rotate left by 1.\n5. Reverse the list.\n6. Reverse the list.\n7. Swap positions 4 and 5 (1-based).\n8. Rotate left by 3.\n9. Rotate left by 4.\n10. Rotate left by 1.\n11. Remove the first item.\n12. Reverse the list.\n13. Reverse the list.\n14. Swap positions 4 and 1 (1-based).\n15. Append b at the end.\n\nGive the final list as comma-separated items, or EMPTY. End your reply with one line: ANSWER: <final answer>",
  "answer": "Q,W,X,e,b"
 },
 {
  "id": "queue-k15-s59",
  "prompt": "A list starts as [V,Z,P,U,Y]. Apply the steps in order.\n\n1. Rotate left by 4.\n2. Rotate left by 1.\n3. Reverse the list.\n4. Swap positions 2 and 4 (1-based).\n5. Reverse the list.\n6. Remove the first item.\n7. Append b at the end.\n8. Append e at the end.\n9. Rotate left by 3.\n10. Reverse the list.\n11. Rotate left by 3.\n12. Append f at the end.\n13. Rotate left by 1.\n14. Reverse the list.\n15. Rotate left by 4.\n\nGive the final list as comma-separated items, or EMPTY. End your reply with one line: ANSWER: <final answer>",
  "answer": "Z,Y,b,e,f,U,P"
 },
 {
  "id": "strings-k15-s11",
  "prompt": "A string starts as 'aadbcccba'. Apply the steps in order. If the letter is absent, the step does nothing.\n\n1. Replace the first 'a' with 'c'.\n2. Replace the first 'd' with 'c'.\n3. Replace the first 'c' with 'd'.\n4. Replace the first 'a' with 'c'.\n5. Replace the first 'c' with 'c'.\n6. Replace the first 'c' with 'c'.\n7. Replace the first 'b' with 'a'.\n8. Replace the first 'b' with 'a'.\n9. Replace the first 'a' with 'd'.\n10. Replace the first 'b' with 'b'.\n11. Replace the first 'a' with 'd'.\n12. Replace the first 'a' with 'b'.\n13. Replace the first 'c' with 'b'.\n14. Replace the first 'd' with 'd'.\n15. Replace the first 'a' with 'c'.\n\nGive the final string. End your reply with one line: ANSWER: <final answer>",
  "answer": "dbcdcccdb"
 },
 {
  "id": "strings-k15-s23",
  "prompt": "A string starts as 'ccdcadaab'. Apply the steps in order. If the letter is absent, the step does nothing.\n\n1. Replace the first 'd' with 'b'.\n2. Replace the first 'b' with 'a'.\n3. Replace the first 'd' with 'a'.\n4. Replace the first 'c' with 'd'.\n5. Replace the first 'b' with 'd'.\n6. Replace the first 'b' with 'a'.\n7. Replace the first 'd' with 'd'.\n8. Replace the first 'd' with 'c'.\n9. Replace the first 'd' with 'b'.\n10. Replace the first 'd' with 'd'.\n11. Replace the first 'b' with 'b'.\n12. Replace the first 'd' with 'b'.\n13. Replace the first 'a' with 'd'.\n14. Replace the first 'd' with 'b'.\n15. Replace the first 'd' with 'b'.\n\nGive the final string. End your reply with one line: ANSWER: <final answer>",
  "answer": "ccbcaaaab"
 },
 {
  "id": "strings-k15-s37",
  "prompt": "A string starts as 'dbacaabcb'. Apply the steps in order. If the letter is absent, the step does nothing.\n\n1. Replace the first 'b' with 'a'.\n2. Replace the first 'c' with 'd'.\n3. Replace the first 'd' with 'd'.\n4. Replace the first 'c' with 'd'.\n5. Replace the first 'd' with 'd'.\n6. Replace the first 'a' with 'b'.\n7. Replace the first 'a' with 'b'.\n8. Replace the first 'a' with 'a'.\n9. Replace the first 'c' with 'a'.\n10. Replace the first 'd' with 'a'.\n11. Replace the first 'c' with 'c'.\n12. Replace the first 'a' with 'b'.\n13. Replace the first 'd' with 'a'.\n14. Replace the first 'd' with 'd'.\n15. Replace the first 'a' with 'd'.\n\nGive the final string. End your reply with one line: ANSWER: <final answer>",
  "answer": "bbbdaabdb"
 },
 {
  "id": "strings-k15-s41",
  "prompt": "A string starts as 'cadcaddab'. Apply the steps in order. If the letter is absent, the step does nothing.\n\n1. Replace the first 'c' with 'c'.\n2. Replace the first 'd' with 'd'.\n3. Replace the first 'd' with 'd'.\n4. Replace the first 'a' with 'a'.\n5. Replace the first 'c' with 'c'.\n6. Replace the first 'b' with 'a'.\n7. Replace the first 'b' with 'b'.\n8. Replace the first 'a' with 'a'.\n9. Replace the first 'b' with 'd'.\n10. Replace the first 'd' with 'a'.\n11. Replace the first 'b' with 'b'.\n12. Replace the first 'a' with 'a'.\n13. Replace the first 'b' with 'a'.\n14. Replace the first 'a' with 'c'.\n15. Replace the first 'b' with 'b'.\n\nGive the final string. End your reply with one line: ANSWER: <final answer>",
  "answer": "ccacaddaa"
 },
 {
  "id": "strings-k15-s59",
  "prompt": "A string starts as 'bbacbbccc'. Apply the steps in order. If the letter is absent, the step does nothing.\n\n1. Replace the first 'd' with 'b'.\n2. Replace the first 'c' with 'c'.\n3. Replace the first 'b' with 'a'.\n4. Replace the first 'b' with 'c'.\n5. Replace the first 'd' with 'a'.\n6. Replace the first 'c' with 'c'.\n7. Replace the first 'a' with 'a'.\n8. Replace the first 'd' with 'b'.\n9. Replace the first 'd' with 'c'.\n10. Replace the first 'a' with 'd'.\n11. Replace the first 'b' with 'c'.\n12. Replace the first 'a' with 'b'.\n13. Replace the first 'a' with 'b'.\n14. Replace the first 'd' with 'c'.\n15. Replace the first 'a' with 'd'.\n\nGive the final string. End your reply with one line: ANSWER: <final answer>",
  "answer": "ccbccbccc"
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
@kbench.task(name="ladder-item-k15", store_task=False)
def ladder_item_k15(llm, prompt: str, answer: str) -> bool:
    out = llm.prompt(prompt)
    return _norm(_extract(out)) == _norm(answer)


# %%
@kbench.task(name="ladder-k15")
def ladder_k15(llm) -> float:
    df = pd.DataFrame(ROWS)
    results = ladder_item_k15.evaluate(llm=[llm], evaluation_data=df[["prompt", "answer"]], n_jobs=8, on_failure="continue", max_attempts=2)
    scores = results.completed_runs.as_dataframe().result
    return float(scores.mean())


ladder_k15.run(kbench.llm)
