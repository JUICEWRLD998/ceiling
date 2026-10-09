# %%
import kaggle_benchmarks as kbench
import pandas as pd

# Ladder, rung k=22: 15 generated state-tracking items (ledger, queue, strings), exact-match scoring, no LLM judge.
# Generator and tests: https://github.com/JUICEWRLD998/ceiling (bench/ladder_gen.py)
ROWS = [
 {
  "id": "ledger-k22-s11",
  "prompt": "Accounts A, B, C start with A=68, B=88, C=25. Apply the steps in order. If the source account holds less than the amount, that step does nothing.\n\n1. Move 16 from C to A.\n2. Move 17 from A to C.\n3. Move 47 from A to C.\n4. Move 48 from B to C.\n5. Move 48 from B to A.\n6. Move 16 from B to A.\n7. Move 11 from B to A.\n8. Move 13 from A to B.\n9. Move 43 from C to A.\n10. Move 36 from C to B.\n11. Move 21 from A to C.\n12. Move 58 from B to A.\n13. Move 6 from C to B.\n14. Move 56 from B to C.\n15. Move 18 from A to C.\n16. Move 53 from A to C.\n17. Move 36 from A to C.\n18. Move 58 from B to C.\n19. Move 17 from B to C.\n20. Move 56 from B to C.\n21. Move 12 from C to A.\n22. Move 20 from A to C.\n\nGive the final balances as A=..,B=..,C=... End your reply with one line: ANSWER: <final answer>",
  "answer": "A=19,B=10,C=152"
 },
 {
  "id": "ledger-k22-s23",
  "prompt": "Accounts A, B, C start with A=56, B=27, C=52. Apply the steps in order. If the source account holds less than the amount, that step does nothing.\n\n1. Move 17 from B to A.\n2. Move 26 from A to C.\n3. Move 60 from A to C.\n4. Move 37 from C to A.\n5. Move 43 from B to C.\n6. Move 55 from C to A.\n7. Move 26 from C to B.\n8. Move 41 from A to B.\n9. Move 14 from B to A.\n10. Move 59 from C to B.\n11. Move 36 from C to B.\n12. Move 29 from A to C.\n13. Move 14 from A to C.\n14. Move 8 from B to C.\n15. Move 43 from C to A.\n16. Move 17 from A to B.\n17. Move 52 from C to A.\n18. Move 25 from A to B.\n19. Move 31 from C to A.\n20. Move 50 from A to B.\n21. Move 23 from B to A.\n22. Move 40 from A to B.\n\nGive the final balances as A=..,B=..,C=... End your reply with one line: ANSWER: <final answer>",
  "answer": "A=38,B=74,C=23"
 },
 {
  "id": "ledger-k22-s37",
  "prompt": "Accounts A, B, C start with A=87, B=84, C=88. Apply the steps in order. If the source account holds less than the amount, that step does nothing.\n\n1. Move 41 from A to C.\n2. Move 58 from B to A.\n3. Move 52 from B to A.\n4. Move 56 from C to B.\n5. Move 21 from C to A.\n6. Move 39 from C to B.\n7. Move 42 from B to A.\n8. Move 44 from C to A.\n9. Move 10 from C to B.\n10. Move 35 from A to B.\n11. Move 46 from B to C.\n12. Move 44 from B to A.\n13. Move 40 from A to B.\n14. Move 51 from C to A.\n15. Move 38 from C to B.\n16. Move 35 from C to A.\n17. Move 53 from C to A.\n18. Move 12 from A to B.\n19. Move 50 from B to A.\n20. Move 24 from A to B.\n21. Move 56 from A to B.\n22. Move 45 from A to C.\n\nGive the final balances as A=..,B=..,C=... End your reply with one line: ANSWER: <final answer>",
  "answer": "A=49,B=154,C=56"
 },
 {
  "id": "ledger-k22-s41",
  "prompt": "Accounts A, B, C start with A=29, B=81, C=57. Apply the steps in order. If the source account holds less than the amount, that step does nothing.\n\n1. Move 57 from B to C.\n2. Move 6 from C to A.\n3. Move 32 from A to C.\n4. Move 22 from A to B.\n5. Move 46 from A to C.\n6. Move 57 from B to C.\n7. Move 57 from B to A.\n8. Move 28 from C to B.\n9. Move 56 from A to C.\n10. Move 43 from B to C.\n11. Move 14 from A to B.\n12. Move 19 from A to B.\n13. Move 5 from C to A.\n14. Move 17 from C to B.\n15. Move 55 from A to C.\n16. Move 60 from B to A.\n17. Move 8 from B to A.\n18. Move 23 from C to B.\n19. Move 22 from C to B.\n20. Move 22 from C to A.\n21. Move 43 from A to C.\n22. Move 31 from B to A.\n\nGive the final balances as A=..,B=..,C=... End your reply with one line: ANSWER: <final answer>",
  "answer": "A=69,B=32,C=66"
 },
 {
  "id": "ledger-k22-s59",
  "prompt": "Accounts A, B, C start with A=59, B=23, C=23. Apply the steps in order. If the source account holds less than the amount, that step does nothing.\n\n1. Move 55 from C to A.\n2. Move 10 from A to B.\n3. Move 20 from A to C.\n4. Move 41 from B to C.\n5. Move 39 from A to B.\n6. Move 27 from B to A.\n7. Move 34 from B to A.\n8. Move 36 from C to A.\n9. Move 31 from C to A.\n10. Move 46 from C to B.\n11. Move 11 from A to B.\n12. Move 12 from C to B.\n13. Move 30 from B to A.\n14. Move 53 from B to A.\n15. Move 37 from B to A.\n16. Move 39 from C to B.\n17. Move 58 from C to B.\n18. Move 33 from B to C.\n19. Move 37 from C to B.\n20. Move 28 from A to C.\n21. Move 35 from B to A.\n22. Move 28 from A to C.\n\nGive the final balances as A=..,B=..,C=... End your reply with one line: ANSWER: <final answer>",
  "answer": "A=25,B=17,C=63"
 },
 {
  "id": "queue-k22-s11",
  "prompt": "A list starts as [U,R,T,Q,S]. Apply the steps in order.\n\n1. Reverse the list.\n2. Append g at the end.\n3. Reverse the list.\n4. Swap positions 3 and 5 (1-based).\n5. Append b at the end.\n6. Swap positions 5 and 3 (1-based).\n7. Append d at the end.\n8. Append c at the end.\n9. Swap positions 8 and 9 (1-based).\n10. Rotate left by 2.\n11. Append a at the end.\n12. Append b at the end.\n13. Remove the first item.\n14. Rotate left by 3.\n15. Remove the first item.\n16. Reverse the list.\n17. Reverse the list.\n18. Remove the first item.\n19. Reverse the list.\n20. Swap positions 3 and 2 (1-based).\n21. Reverse the list.\n22. Append g at the end.\n\nGive the final list as comma-separated items, or EMPTY. End your reply with one line: ANSWER: <final answer>",
  "answer": "d,g,U,a,b,Q,T,S,g"
 },
 {
  "id": "queue-k22-s23",
  "prompt": "A list starts as [S,R,W,V,Z]. Apply the steps in order.\n\n1. Swap positions 5 and 1 (1-based).\n2. Remove the first item.\n3. Reverse the list.\n4. Rotate left by 4.\n5. Append c at the end.\n6. Append f at the end.\n7. Append b at the end.\n8. Remove the first item.\n9. Swap positions 4 and 1 (1-based).\n10. Swap positions 3 and 6 (1-based).\n11. Append c at the end.\n12. Append h at the end.\n13. Reverse the list.\n14. Remove the first item.\n15. Swap positions 5 and 4 (1-based).\n16. Reverse the list.\n17. Swap positions 6 and 2 (1-based).\n18. Reverse the list.\n19. Rotate left by 2.\n20. Append a at the end.\n21. Remove the first item.\n22. Rotate left by 3.\n\nGive the final list as comma-separated items, or EMPTY. End your reply with one line: ANSWER: <final answer>",
  "answer": "c,c,W,a,b,V,R"
 },
 {
  "id": "queue-k22-s37",
  "prompt": "A list starts as [R,Y,U,W,S]. Apply the steps in order.\n\n1. Reverse the list.\n2. Swap positions 5 and 1 (1-based).\n3. Rotate left by 2.\n4. Append h at the end.\n5. Rotate left by 2.\n6. Swap positions 1 and 6 (1-based).\n7. Rotate left by 3.\n8. Reverse the list.\n9. Append g at the end.\n10. Reverse the list.\n11. Remove the first item.\n12. Reverse the list.\n13. Remove the first item.\n14. Remove the first item.\n15. Reverse the list.\n16. Append h at the end.\n17. Reverse the list.\n18. Remove the first item.\n19. Remove the first item.\n20. Swap positions 1 and 3 (1-based).\n21. Remove the first item.\n22. Rotate left by 3.\n\nGive the final list as comma-separated items, or EMPTY. End your reply with one line: ANSWER: <final answer>",
  "answer": "S,U"
 },
 {
  "id": "queue-k22-s41",
  "prompt": "A list starts as [R,U,W,V,P]. Apply the steps in order.\n\n1. Rotate left by 4.\n2. Remove the first item.\n3. Swap positions 1 and 3 (1-based).\n4. Swap positions 2 and 1 (1-based).\n5. Reverse the list.\n6. Rotate left by 4.\n7. Swap positions 2 and 4 (1-based).\n8. Append f at the end.\n9. Append f at the end.\n10. Swap positions 3 and 4 (1-based).\n11. Reverse the list.\n12. Remove the first item.\n13. Swap positions 4 and 2 (1-based).\n14. Rotate left by 2.\n15. Append c at the end.\n16. Rotate left by 2.\n17. Reverse the list.\n18. Swap positions 2 and 1 (1-based).\n19. Remove the first item.\n20. Rotate left by 1.\n21. Append g at the end.\n22. Swap positions 3 and 5 (1-based).\n\nGive the final list as comma-separated items, or EMPTY. End your reply with one line: ANSWER: <final answer>",
  "answer": "c,U,W,V,f,g"
 },
 {
  "id": "queue-k22-s59",
  "prompt": "A list starts as [Y,W,Q,U,T]. Apply the steps in order.\n\n1. Rotate left by 2.\n2. Append e at the end.\n3. Rotate left by 2.\n4. Reverse the list.\n5. Rotate left by 3.\n6. Remove the first item.\n7. Swap positions 5 and 3 (1-based).\n8. Reverse the list.\n9. Remove the first item.\n10. Reverse the list.\n11. Append h at the end.\n12. Rotate left by 3.\n13. Append g at the end.\n14. Append f at the end.\n15. Swap positions 4 and 2 (1-based).\n16. Remove the first item.\n17. Append h at the end.\n18. Rotate left by 3.\n19. Reverse the list.\n20. Rotate left by 2.\n21. Rotate left by 4.\n22. Remove the first item.\n\nGive the final list as comma-separated items, or EMPTY. End your reply with one line: ANSWER: <final answer>",
  "answer": "h,Y,T,h,f,g"
 },
 {
  "id": "strings-k22-s11",
  "prompt": "A string starts as 'baacacbbc'. Apply the steps in order. If the letter is absent, the step does nothing.\n\n1. Replace the first 'a' with 'b'.\n2. Replace the first 'b' with 'c'.\n3. Replace the first 'c' with 'a'.\n4. Replace the first 'a' with 'd'.\n5. Replace the first 'b' with 'd'.\n6. Replace the first 'b' with 'd'.\n7. Replace the first 'd' with 'c'.\n8. Replace the first 'c' with 'a'.\n9. Replace the first 'a' with 'b'.\n10. Replace the first 'd' with 'c'.\n11. Replace the first 'a' with 'b'.\n12. Replace the first 'd' with 'a'.\n13. Replace the first 'c' with 'a'.\n14. Replace the first 'c' with 'd'.\n15. Replace the first 'a' with 'a'.\n16. Replace the first 'a' with 'd'.\n17. Replace the first 'b' with 'd'.\n18. Replace the first 'c' with 'a'.\n19. Replace the first 'b' with 'a'.\n20. Replace the first 'c' with 'c'.\n21. Replace the first 'c' with 'a'.\n22. Replace the first 'b' with 'a'.\n\nGive the final string. End your reply with one line: ANSWER: <final answer>",
  "answer": "ddadaaaaa"
 },
 {
  "id": "strings-k22-s23",
  "prompt": "A string starts as 'acaccdada'. Apply the steps in order. If the letter is absent, the step does nothing.\n\n1. Replace the first 'b' with 'c'.\n2. Replace the first 'b' with 'b'.\n3. Replace the first 'b' with 'b'.\n4. Replace the first 'd' with 'b'.\n5. Replace the first 'd' with 'a'.\n6. Replace the first 'd' with 'b'.\n7. Replace the first 'b' with 'a'.\n8. Replace the first 'c' with 'd'.\n9. Replace the first 'd' with 'b'.\n10. Replace the first 'd' with 'd'.\n11. Replace the first 'b' with 'd'.\n12. Replace the first 'b' with 'b'.\n13. Replace the first 'c' with 'b'.\n14. Replace the first 'd' with 'c'.\n15. Replace the first 'b' with 'a'.\n16. Replace the first 'a' with 'c'.\n17. Replace the first 'c' with 'a'.\n18. Replace the first 'a' with 'b'.\n19. Replace the first 'b' with 'b'.\n20. Replace the first 'b' with 'b'.\n21. Replace the first 'a' with 'a'.\n22. Replace the first 'b' with 'c'.\n\nGive the final string. End your reply with one line: ANSWER: <final answer>",
  "answer": "ccaacaaaa"
 },
 {
  "id": "strings-k22-s37",
  "prompt": "A string starts as 'adcbadaca'. Apply the steps in order. If the letter is absent, the step does nothing.\n\n1. Replace the first 'd' with 'b'.\n2. Replace the first 'a' with 'd'.\n3. Replace the first 'a' with 'b'.\n4. Replace the first 'd' with 'c'.\n5. Replace the first 'c' with 'd'.\n6. Replace the first 'd' with 'b'.\n7. Replace the first 'b' with 'a'.\n8. Replace the first 'd' with 'b'.\n9. Replace the first 'c' with 'd'.\n10. Replace the first 'd' with 'b'.\n11. Replace the first 'c' with 'b'.\n12. Replace the first 'c' with 'd'.\n13. Replace the first 'c' with 'a'.\n14. Replace the first 'c' with 'c'.\n15. Replace the first 'a' with 'c'.\n16. Replace the first 'a' with 'd'.\n17. Replace the first 'c' with 'd'.\n18. Replace the first 'c' with 'd'.\n19. Replace the first 'b' with 'd'.\n20. Replace the first 'd' with 'd'.\n21. Replace the first 'a' with 'c'.\n22. Replace the first 'd' with 'd'.\n\nGive the final string. End your reply with one line: ANSWER: <final answer>",
  "answer": "ddbbbbdbc"
 },
 {
  "id": "strings-k22-s41",
  "prompt": "A string starts as 'cadaadcba'. Apply the steps in order. If the letter is absent, the step does nothing.\n\n1. Replace the first 'd' with 'a'.\n2. Replace the first 'd' with 'c'.\n3. Replace the first 'c' with 'c'.\n4. Replace the first 'c' with 'b'.\n5. Replace the first 'a' with 'a'.\n6. Replace the first 'd' with 'b'.\n7. Replace the first 'b' with 'a'.\n8. Replace the first 'c' with 'b'.\n9. Replace the first 'a' with 'a'.\n10. Replace the first 'c' with 'd'.\n11. Replace the first 'b' with 'a'.\n12. Replace the first 'a' with 'a'.\n13. Replace the first 'c' with 'b'.\n14. Replace the first 'a' with 'c'.\n15. Replace the first 'b' with 'c'.\n16. Replace the first 'd' with 'd'.\n17. Replace the first 'd' with 'b'.\n18. Replace the first 'b' with 'c'.\n19. Replace the first 'b' with 'd'.\n20. Replace the first 'b' with 'c'.\n21. Replace the first 'd' with 'a'.\n22. Replace the first 'c' with 'a'.\n\nGive the final string. End your reply with one line: ANSWER: <final answer>",
  "answer": "aaaaaacca"
 },
 {
  "id": "strings-k22-s59",
  "prompt": "A string starts as 'caaadabbd'. Apply the steps in order. If the letter is absent, the step does nothing.\n\n1. Replace the first 'b' with 'c'.\n2. Replace the first 'c' with 'c'.\n3. Replace the first 'b' with 'c'.\n4. Replace the first 'b' with 'a'.\n5. Replace the first 'b' with 'd'.\n6. Replace the first 'd' with 'b'.\n7. Replace the first 'a' with 'd'.\n8. Replace the first 'd' with 'c'.\n9. Replace the first 'a' with 'c'.\n10. Replace the first 'b' with 'b'.\n11. Replace the first 'd' with 'a'.\n12. Replace the first 'b' with 'd'.\n13. Replace the first 'c' with 'c'.\n14. Replace the first 'a' with 'c'.\n15. Replace the first 'd' with 'b'.\n16. Replace the first 'd' with 'c'.\n17. Replace the first 'b' with 'a'.\n18. Replace the first 'b' with 'd'.\n19. Replace the first 'c' with 'a'.\n20. Replace the first 'b' with 'c'.\n21. Replace the first 'd' with 'a'.\n22. Replace the first 'd' with 'b'.\n\nGive the final string. End your reply with one line: ANSWER: <final answer>",
  "answer": "acccaacca"
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
@kbench.task(name="ladder-item-k22", store_task=False)
def ladder_item_k22(llm, prompt: str, answer: str) -> bool:
    out = llm.prompt(prompt)
    return _norm(_extract(out)) == _norm(answer)


# %%
@kbench.task(name="ladder-k22")
def ladder_k22(llm) -> float:
    df = pd.DataFrame(ROWS)
    results = ladder_item_k22.evaluate(llm=[llm], evaluation_data=df[["prompt", "answer"]], n_jobs=8, on_failure="continue", max_attempts=2)
    scores = results.completed_runs.as_dataframe().result
    return float(scores.mean())


ladder_k22.run(kbench.llm)
