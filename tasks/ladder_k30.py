# %%
import kaggle_benchmarks as kbench
import pandas as pd

# Ladder, rung k=30: 15 generated state-tracking items (ledger, queue, strings), exact-match scoring, no LLM judge.
# Generator and tests: https://github.com/JUICEWRLD998/ceiling (bench/ladder_gen.py)
ROWS = [
 {
  "id": "ledger-k30-s11",
  "prompt": "Accounts A, B, C start with A=86, B=86, C=34. Apply the steps in order. If the source account holds less than the amount, that step does nothing.\n\n1. Move 45 from A to C.\n2. Move 12 from B to A.\n3. Move 23 from B to C.\n4. Move 53 from C to B.\n5. Move 34 from B to A.\n6. Move 25 from B to A.\n7. Move 47 from C to A.\n8. Move 9 from C to A.\n9. Move 23 from C to B.\n10. Move 17 from A to B.\n11. Move 30 from B to A.\n12. Move 17 from B to A.\n13. Move 22 from A to C.\n14. Move 50 from C to B.\n15. Move 24 from C to B.\n16. Move 58 from C to A.\n17. Move 5 from C to B.\n18. Move 19 from C to B.\n19. Move 35 from A to B.\n20. Move 59 from C to B.\n21. Move 51 from A to C.\n22. Move 8 from A to C.\n23. Move 40 from B to C.\n24. Move 50 from C to A.\n25. Move 45 from A to B.\n26. Move 12 from B to C.\n27. Move 28 from B to A.\n28. Move 56 from A to B.\n29. Move 6 from A to B.\n30. Move 42 from B to A.\n\nGive the final balances as A=..,B=..,C=... End your reply with one line: ANSWER: <final answer>",
  "answer": "A=86,B=59,C=61"
 },
 {
  "id": "ledger-k30-s23",
  "prompt": "Accounts A, B, C start with A=85, B=60, C=70. Apply the steps in order. If the source account holds less than the amount, that step does nothing.\n\n1. Move 25 from B to C.\n2. Move 53 from B to C.\n3. Move 47 from C to B.\n4. Move 51 from B to C.\n5. Move 50 from B to A.\n6. Move 46 from C to A.\n7. Move 29 from B to C.\n8. Move 55 from C to B.\n9. Move 39 from C to B.\n10. Move 51 from C to A.\n11. Move 21 from C to B.\n12. Move 55 from A to C.\n13. Move 15 from B to A.\n14. Move 46 from C to A.\n15. Move 15 from A to B.\n16. Move 44 from C to A.\n17. Move 40 from B to A.\n18. Move 29 from C to B.\n19. Move 25 from B to A.\n20. Move 15 from C to B.\n21. Move 18 from C to B.\n22. Move 9 from B to C.\n23. Move 39 from A to B.\n24. Move 52 from C to A.\n25. Move 34 from C to B.\n26. Move 29 from B to A.\n27. Move 54 from C to A.\n28. Move 57 from A to B.\n29. Move 17 from B to C.\n30. Move 8 from B to C.\n\nGive the final balances as A=..,B=..,C=... End your reply with one line: ANSWER: <final answer>",
  "answer": "A=120,B=61,C=34"
 },
 {
  "id": "ledger-k30-s37",
  "prompt": "Accounts A, B, C start with A=79, B=87, C=79. Apply the steps in order. If the source account holds less than the amount, that step does nothing.\n\n1. Move 12 from A to B.\n2. Move 11 from C to A.\n3. Move 22 from C to A.\n4. Move 29 from C to B.\n5. Move 26 from C to A.\n6. Move 28 from B to C.\n7. Move 7 from A to B.\n8. Move 34 from A to C.\n9. Move 17 from B to C.\n10. Move 14 from B to A.\n11. Move 50 from A to B.\n12. Move 55 from A to B.\n13. Move 6 from A to C.\n14. Move 27 from B to C.\n15. Move 35 from C to B.\n16. Move 43 from B to C.\n17. Move 49 from C to A.\n18. Move 38 from B to A.\n19. Move 8 from B to C.\n20. Move 35 from C to A.\n21. Move 25 from C to B.\n22. Move 16 from A to C.\n23. Move 5 from C to A.\n24. Move 43 from A to C.\n25. Move 19 from C to B.\n26. Move 24 from B to C.\n27. Move 33 from B to C.\n28. Move 50 from C to B.\n29. Move 59 from C to B.\n30. Move 59 from B to C.\n\nGive the final balances as A=..,B=..,C=... End your reply with one line: ANSWER: <final answer>",
  "answer": "A=85,B=82,C=78"
 },
 {
  "id": "ledger-k30-s41",
  "prompt": "Accounts A, B, C start with A=38, B=76, C=52. Apply the steps in order. If the source account holds less than the amount, that step does nothing.\n\n1. Move 56 from A to C.\n2. Move 42 from A to C.\n3. Move 30 from B to C.\n4. Move 43 from B to A.\n5. Move 44 from C to B.\n6. Move 57 from B to C.\n7. Move 48 from A to B.\n8. Move 10 from C to A.\n9. Move 5 from C to B.\n10. Move 54 from C to B.\n11. Move 5 from B to C.\n12. Move 12 from A to C.\n13. Move 26 from B to C.\n14. Move 23 from A to C.\n15. Move 29 from A to B.\n16. Move 31 from C to B.\n17. Move 32 from B to C.\n18. Move 12 from A to B.\n19. Move 57 from A to C.\n20. Move 10 from B to C.\n21. Move 57 from A to B.\n22. Move 34 from C to B.\n23. Move 46 from B to C.\n24. Move 29 from A to C.\n25. Move 10 from C to A.\n26. Move 13 from B to A.\n27. Move 23 from A to B.\n28. Move 46 from B to C.\n29. Move 6 from C to B.\n30. Move 53 from B to A.\n\nGive the final balances as A=..,B=..,C=... End your reply with one line: ANSWER: <final answer>",
  "answer": "A=8,B=16,C=142"
 },
 {
  "id": "ledger-k30-s59",
  "prompt": "Accounts A, B, C start with A=25, B=46, C=48. Apply the steps in order. If the source account holds less than the amount, that step does nothing.\n\n1. Move 24 from A to B.\n2. Move 39 from B to A.\n3. Move 8 from B to A.\n4. Move 5 from A to C.\n5. Move 6 from A to C.\n6. Move 59 from C to B.\n7. Move 9 from B to C.\n8. Move 36 from C to A.\n9. Move 58 from C to B.\n10. Move 46 from C to A.\n11. Move 30 from B to C.\n12. Move 12 from A to B.\n13. Move 18 from C to A.\n14. Move 31 from C to B.\n15. Move 6 from B to A.\n16. Move 20 from A to C.\n17. Move 7 from A to B.\n18. Move 37 from C to A.\n19. Move 30 from C to B.\n20. Move 44 from C to B.\n21. Move 59 from C to A.\n22. Move 26 from A to C.\n23. Move 43 from A to B.\n24. Move 19 from A to C.\n25. Move 54 from B to A.\n26. Move 31 from A to B.\n27. Move 52 from B to C.\n28. Move 12 from A to B.\n29. Move 22 from A to C.\n30. Move 39 from B to A.\n\nGive the final balances as A=..,B=..,C=... End your reply with one line: ANSWER: <final answer>",
  "answer": "A=42,B=6,C=71"
 },
 {
  "id": "queue-k30-s11",
  "prompt": "A list starts as [W,Q,X,U,P]. Apply the steps in order.\n\n1. Reverse the list.\n2. Append h at the end.\n3. Rotate left by 3.\n4. Rotate left by 2.\n5. Swap positions 3 and 6 (1-based).\n6. Remove the first item.\n7. Swap positions 1 and 3 (1-based).\n8. Swap positions 4 and 1 (1-based).\n9. Rotate left by 2.\n10. Rotate left by 2.\n11. Append e at the end.\n12. Append e at the end.\n13. Append a at the end.\n14. Swap positions 3 and 1 (1-based).\n15. Reverse the list.\n16. Reverse the list.\n17. Swap positions 8 and 4 (1-based).\n18. Append a at the end.\n19. Reverse the list.\n20. Remove the first item.\n21. Append f at the end.\n22. Remove the first item.\n23. Rotate left by 4.\n24. Reverse the list.\n25. Swap positions 4 and 1 (1-based).\n26. Swap positions 5 and 7 (1-based).\n27. Swap positions 3 and 1 (1-based).\n28. Reverse the list.\n29. Append b at the end.\n30. Rotate left by 3.\n\nGive the final list as comma-separated items, or EMPTY. End your reply with one line: ANSWER: <final answer>",
  "answer": "Q,a,e,X,e,b,U,f,W"
 },
 {
  "id": "queue-k30-s23",
  "prompt": "A list starts as [Z,W,R,Q,P]. Apply the steps in order.\n\n1. Append g at the end.\n2. Swap positions 5 and 6 (1-based).\n3. Remove the first item.\n4. Append b at the end.\n5. Remove the first item.\n6. Rotate left by 3.\n7. Remove the first item.\n8. Reverse the list.\n9. Rotate left by 2.\n10. Rotate left by 2.\n11. Swap positions 2 and 1 (1-based).\n12. Rotate left by 1.\n13. Rotate left by 3.\n14. Reverse the list.\n15. Remove the first item.\n16. Swap positions 3 and 1 (1-based).\n17. Append b at the end.\n18. Swap positions 2 and 3 (1-based).\n19. Swap positions 3 and 4 (1-based).\n20. Rotate left by 1.\n21. Swap positions 1 and 4 (1-based).\n22. Remove the first item.\n23. Append e at the end.\n24. Append b at the end.\n25. Remove the first item.\n26. Swap positions 1 and 2 (1-based).\n27. Rotate left by 1.\n28. Append f at the end.\n29. Remove the first item.\n30. Swap positions 3 and 1 (1-based).\n\nGive the final list as comma-separated items, or EMPTY. End your reply with one line: ANSWER: <final answer>",
  "answer": "R,b,e,f"
 },
 {
  "id": "queue-k30-s37",
  "prompt": "A list starts as [R,X,T,Q,W]. Apply the steps in order.\n\n1. Swap positions 1 and 3 (1-based).\n2. Reverse the list.\n3. Reverse the list.\n4. Reverse the list.\n5. Append b at the end.\n6. Rotate left by 4.\n7. Append d at the end.\n8. Append d at the end.\n9. Rotate left by 1.\n10. Reverse the list.\n11. Reverse the list.\n12. Swap positions 4 and 1 (1-based).\n13. Swap positions 2 and 5 (1-based).\n14. Append b at the end.\n15. Swap positions 6 and 4 (1-based).\n16. Remove the first item.\n17. Remove the first item.\n18. Rotate left by 1.\n19. Rotate left by 1.\n20. Swap positions 4 and 1 (1-based).\n21. Rotate left by 4.\n22. Rotate left by 1.\n23. Reverse the list.\n24. Append g at the end.\n25. Reverse the list.\n26. Remove the first item.\n27. Remove the first item.\n28. Swap positions 2 and 6 (1-based).\n29. Rotate left by 1.\n30. Rotate left by 4.\n\nGive the final list as comma-separated items, or EMPTY. End your reply with one line: ANSWER: <final answer>",
  "answer": "T,d,b,b,d,W"
 },
 {
  "id": "queue-k30-s41",
  "prompt": "A list starts as [Q,U,P,Y,T]. Apply the steps in order.\n\n1. Remove the first item.\n2. Rotate left by 4.\n3. Remove the first item.\n4. Append f at the end.\n5. Reverse the list.\n6. Swap positions 1 and 3 (1-based).\n7. Rotate left by 4.\n8. Swap positions 1 and 2 (1-based).\n9. Rotate left by 1.\n10. Append c at the end.\n11. Swap positions 3 and 2 (1-based).\n12. Append h at the end.\n13. Remove the first item.\n14. Append c at the end.\n15. Rotate left by 3.\n16. Rotate left by 1.\n17. Remove the first item.\n18. Swap positions 1 and 3 (1-based).\n19. Rotate left by 4.\n20. Reverse the list.\n21. Reverse the list.\n22. Swap positions 5 and 2 (1-based).\n23. Append a at the end.\n24. Remove the first item.\n25. Append d at the end.\n26. Append c at the end.\n27. Remove the first item.\n28. Reverse the list.\n29. Reverse the list.\n30. Append a at the end.\n\nGive the final list as comma-separated items, or EMPTY. End your reply with one line: ANSWER: <final answer>",
  "answer": "P,c,f,a,d,c,a"
 },
 {
  "id": "queue-k30-s59",
  "prompt": "A list starts as [S,U,W,Q,R]. Apply the steps in order.\n\n1. Append e at the end.\n2. Append c at the end.\n3. Reverse the list.\n4. Rotate left by 3.\n5. Append e at the end.\n6. Reverse the list.\n7. Remove the first item.\n8. Append f at the end.\n9. Reverse the list.\n10. Reverse the list.\n11. Remove the first item.\n12. Remove the first item.\n13. Append b at the end.\n14. Reverse the list.\n15. Remove the first item.\n16. Append d at the end.\n17. Append g at the end.\n18. Append d at the end.\n19. Rotate left by 4.\n20. Reverse the list.\n21. Remove the first item.\n22. Remove the first item.\n23. Remove the first item.\n24. Rotate left by 1.\n25. Remove the first item.\n26. Append b at the end.\n27. Swap positions 2 and 3 (1-based).\n28. Swap positions 6 and 1 (1-based).\n29. Swap positions 1 and 2 (1-based).\n30. Append c at the end.\n\nGive the final list as comma-separated items, or EMPTY. End your reply with one line: ANSWER: <final answer>",
  "answer": "c,b,d,S,f,g,c"
 },
 {
  "id": "strings-k30-s11",
  "prompt": "A string starts as 'abcdddcaa'. Apply the steps in order. If the letter is absent, the step does nothing.\n\n1. Replace the first 'd' with 'a'.\n2. Replace the first 'b' with 'c'.\n3. Replace the first 'b' with 'b'.\n4. Replace the first 'a' with 'a'.\n5. Replace the first 'b' with 'c'.\n6. Replace the first 'd' with 'a'.\n7. Replace the first 'b' with 'b'.\n8. Replace the first 'c' with 'a'.\n9. Replace the first 'd' with 'd'.\n10. Replace the first 'a' with 'a'.\n11. Replace the first 'c' with 'd'.\n12. Replace the first 'd' with 'a'.\n13. Replace the first 'a' with 'c'.\n14. Replace the first 'a' with 'd'.\n15. Replace the first 'a' with 'a'.\n16. Replace the first 'd' with 'b'.\n17. Replace the first 'd' with 'd'.\n18. Replace the first 'a' with 'c'.\n19. Replace the first 'b' with 'c'.\n20. Replace the first 'd' with 'd'.\n21. Replace the first 'd' with 'c'.\n22. Replace the first 'd' with 'd'.\n23. Replace the first 'b' with 'a'.\n24. Replace the first 'b' with 'd'.\n25. Replace the first 'd' with 'd'.\n26. Replace the first 'a' with 'b'.\n27. Replace the first 'b' with 'c'.\n28. Replace the first 'c' with 'c'.\n29. Replace the first 'd' with 'c'.\n30. Replace the first 'd' with 'd'.\n\nGive the final string. End your reply with one line: ANSWER: <final answer>",
  "answer": "ccccaccaa"
 },
 {
  "id": "strings-k30-s23",
  "prompt": "A string starts as 'aabdacadc'. Apply the steps in order. If the letter is absent, the step does nothing.\n\n1. Replace the first 'd' with 'a'.\n2. Replace the first 'd' with 'a'.\n3. Replace the first 'a' with 'b'.\n4. Replace the first 'd' with 'c'.\n5. Replace the first 'a' with 'b'.\n6. Replace the first 'a' with 'b'.\n7. Replace the first 'd' with 'b'.\n8. Replace the first 'a' with 'd'.\n9. Replace the first 'd' with 'b'.\n10. Replace the first 'c' with 'a'.\n11. Replace the first 'b' with 'a'.\n12. Replace the first 'b' with 'b'.\n13. Replace the first 'a' with 'c'.\n14. Replace the first 'c' with 'd'.\n15. Replace the first 'a' with 'c'.\n16. Replace the first 'c' with 'd'.\n17. Replace the first 'c' with 'b'.\n18. Replace the first 'd' with 'd'.\n19. Replace the first 'd' with 'd'.\n20. Replace the first 'c' with 'd'.\n21. Replace the first 'a' with 'b'.\n22. Replace the first 'd' with 'a'.\n23. Replace the first 'b' with 'b'.\n24. Replace the first 'b' with 'a'.\n25. Replace the first 'b' with 'd'.\n26. Replace the first 'a' with 'b'.\n27. Replace the first 'c' with 'c'.\n28. Replace the first 'b' with 'd'.\n29. Replace the first 'a' with 'b'.\n30. Replace the first 'a' with 'a'.\n\nGive the final string. End your reply with one line: ANSWER: <final answer>",
  "answer": "dbdbbdbab"
 },
 {
  "id": "strings-k30-s37",
  "prompt": "A string starts as 'bcaaccccc'. Apply the steps in order. If the letter is absent, the step does nothing.\n\n1. Replace the first 'a' with 'c'.\n2. Replace the first 'd' with 'b'.\n3. Replace the first 'b' with 'c'.\n4. Replace the first 'c' with 'c'.\n5. Replace the first 'd' with 'd'.\n6. Replace the first 'd' with 'd'.\n7. Replace the first 'd' with 'd'.\n8. Replace the first 'd' with 'd'.\n9. Replace the first 'd' with 'a'.\n10. Replace the first 'd' with 'a'.\n11. Replace the first 'b' with 'a'.\n12. Replace the first 'b' with 'a'.\n13. Replace the first 'a' with 'c'.\n14. Replace the first 'c' with 'c'.\n15. Replace the first 'c' with 'c'.\n16. Replace the first 'c' with 'c'.\n17. Replace the first 'a' with 'd'.\n18. Replace the first 'b' with 'a'.\n19. Replace the first 'c' with 'd'.\n20. Replace the first 'c' with 'b'.\n21. Replace the first 'c' with 'd'.\n22. Replace the first 'b' with 'c'.\n23. Replace the first 'd' with 'b'.\n24. Replace the first 'd' with 'a'.\n25. Replace the first 'a' with 'c'.\n26. Replace the first 'd' with 'd'.\n27. Replace the first 'b' with 'b'.\n28. Replace the first 'd' with 'c'.\n29. Replace the first 'b' with 'b'.\n30. Replace the first 'd' with 'c'.\n\nGive the final string. End your reply with one line: ANSWER: <final answer>",
  "answer": "bcccccccc"
 },
 {
  "id": "strings-k30-s41",
  "prompt": "A string starts as 'cbbddacaa'. Apply the steps in order. If the letter is absent, the step does nothing.\n\n1. Replace the first 'd' with 'b'.\n2. Replace the first 'b' with 'a'.\n3. Replace the first 'a' with 'c'.\n4. Replace the first 'c' with 'c'.\n5. Replace the first 'c' with 'd'.\n6. Replace the first 'a' with 'a'.\n7. Replace the first 'c' with 'c'.\n8. Replace the first 'd' with 'd'.\n9. Replace the first 'b' with 'b'.\n10. Replace the first 'd' with 'b'.\n11. Replace the first 'a' with 'b'.\n12. Replace the first 'd' with 'b'.\n13. Replace the first 'c' with 'd'.\n14. Replace the first 'c' with 'c'.\n15. Replace the first 'd' with 'b'.\n16. Replace the first 'a' with 'a'.\n17. Replace the first 'b' with 'd'.\n18. Replace the first 'd' with 'c'.\n19. Replace the first 'a' with 'a'.\n20. Replace the first 'b' with 'd'.\n21. Replace the first 'd' with 'b'.\n22. Replace the first 'a' with 'a'.\n23. Replace the first 'b' with 'd'.\n24. Replace the first 'd' with 'd'.\n25. Replace the first 'b' with 'a'.\n26. Replace the first 'a' with 'b'.\n27. Replace the first 'c' with 'a'.\n28. Replace the first 'a' with 'a'.\n29. Replace the first 'a' with 'b'.\n30. Replace the first 'c' with 'a'.\n\nGive the final string. End your reply with one line: ANSWER: <final answer>",
  "answer": "bdbbbbaaa"
 },
 {
  "id": "strings-k30-s59",
  "prompt": "A string starts as 'dddddcccb'. Apply the steps in order. If the letter is absent, the step does nothing.\n\n1. Replace the first 'a' with 'a'.\n2. Replace the first 'c' with 'b'.\n3. Replace the first 'd' with 'c'.\n4. Replace the first 'b' with 'd'.\n5. Replace the first 'b' with 'd'.\n6. Replace the first 'c' with 'a'.\n7. Replace the first 'd' with 'd'.\n8. Replace the first 'a' with 'a'.\n9. Replace the first 'd' with 'c'.\n10. Replace the first 'c' with 'c'.\n11. Replace the first 'b' with 'b'.\n12. Replace the first 'b' with 'a'.\n13. Replace the first 'd' with 'b'.\n14. Replace the first 'b' with 'a'.\n15. Replace the first 'a' with 'b'.\n16. Replace the first 'd' with 'c'.\n17. Replace the first 'b' with 'a'.\n18. Replace the first 'a' with 'b'.\n19. Replace the first 'c' with 'c'.\n20. Replace the first 'b' with 'b'.\n21. Replace the first 'c' with 'c'.\n22. Replace the first 'd' with 'c'.\n23. Replace the first 'd' with 'a'.\n24. Replace the first 'd' with 'c'.\n25. Replace the first 'd' with 'd'.\n26. Replace the first 'c' with 'b'.\n27. Replace the first 'd' with 'c'.\n28. Replace the first 'd' with 'b'.\n29. Replace the first 'b' with 'd'.\n30. Replace the first 'c' with 'd'.\n\nGive the final string. End your reply with one line: ANSWER: <final answer>",
  "answer": "dbadcaccc"
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
@kbench.task(name="ladder-item-k30", store_task=False)
def ladder_item_k30(llm, prompt: str, answer: str) -> bool:
    out = llm.prompt(prompt)
    return _norm(_extract(out)) == _norm(answer)


# %%
@kbench.task(name="ladder-k30")
def ladder_k30(llm) -> float:
    df = pd.DataFrame(ROWS)
    results = ladder_item_k30.evaluate(llm=[llm], evaluation_data=df[["prompt", "answer"]], n_jobs=8, on_failure="continue", max_attempts=2)
    scores = results.completed_runs.as_dataframe().result
    return float(scores.mean())


ladder_k30.run(kbench.llm)
