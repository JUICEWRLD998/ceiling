"""Ladder: programmatically generated, difficulty-laddered state-tracking items with exact answers.

Three families (ledger, queue, strings) x six rungs (k operations) x five seeds = 90 items. No LLM judge.
Every answer comes from simulating the operations; extract() reads the last 'ANSWER:' line.
"""
import json
import random

RUNGS = [3, 6, 10, 15, 22, 30]
SEEDS = [11, 23, 37, 41, 59]
FAMILIES = ["ledger", "queue", "strings"]


def _ledger(rng, k):
    bal = {"A": rng.randint(20, 90), "B": rng.randint(20, 90), "C": rng.randint(20, 90)}
    start = dict(bal)
    lines = []
    for i in range(1, k + 1):
        src, dst = rng.sample(["A", "B", "C"], 2)
        amt = rng.randint(5, 60)
        lines.append(f"{i}. Move {amt} from {src} to {dst}.")
        if bal[src] >= amt:
            bal[src] -= amt
            bal[dst] += amt
    rules = ("Accounts A, B, C start with A=%d, B=%d, C=%d. Apply the steps in order. "
             "If the source account holds less than the amount, that step does nothing." % (start["A"], start["B"], start["C"]))
    ans = "A=%d,B=%d,C=%d" % (bal["A"], bal["B"], bal["C"])
    return rules, lines, "Give the final balances as A=..,B=..,C=..", ans


def _queue(rng, k):
    items = rng.sample("PQRSTUVWXYZ", 5)
    cur = list(items)
    lines = []
    for i in range(1, k + 1):
        kind = rng.choice(["rotl", "swap", "drop", "add", "rev"])
        if kind == "rotl" and cur:
            n = rng.randint(1, 4)
            lines.append(f"{i}. Rotate left by {n}.")
            m = n % len(cur)
            cur = cur[m:] + cur[:m]
        elif kind == "swap" and len(cur) >= 2:
            a, b = rng.sample(range(1, len(cur) + 1), 2)
            lines.append(f"{i}. Swap positions {a} and {b} (1-based).")
            cur[a - 1], cur[b - 1] = cur[b - 1], cur[a - 1]
        elif kind == "drop" and cur:
            lines.append(f"{i}. Remove the first item.")
            cur = cur[1:]
        elif kind == "rev":
            lines.append(f"{i}. Reverse the list.")
            cur = cur[::-1]
        else:
            ch = rng.choice("abcdefgh")
            lines.append(f"{i}. Append {ch} at the end.")
            cur = cur + [ch]
    rules = "A list starts as [%s]. Apply the steps in order." % ",".join(items)
    ans = ",".join(cur) if cur else "EMPTY"
    return rules, lines, "Give the final list as comma-separated items, or EMPTY", ans


def _strings(rng, k):
    word = "".join(rng.choice("abcd") for _ in range(9))
    cur = word
    lines = []
    for i in range(1, k + 1):
        x = rng.choice("abcd")
        y = rng.choice("abcd")
        lines.append(f"{i}. Replace the first '{x}' with '{y}'.")
        cur = cur.replace(x, y, 1)
    rules = "A string starts as '%s'. Apply the steps in order. If the letter is absent, the step does nothing." % word
    return rules, lines, "Give the final string", cur


_GEN = {"ledger": _ledger, "queue": _queue, "strings": _strings}


def make_item(family, k, seed):
    rng = random.Random(f"{family}-{k}-{seed}")
    rules, lines, ask, ans = _GEN[family](rng, k)
    prompt = rules + "\n\n" + "\n".join(lines) + "\n\n" + ask + ". End your reply with one line: ANSWER: <final answer>"
    return {"id": f"{family}-k{k:02d}-s{seed}", "family": family, "k": k, "prompt": prompt, "answer": ans}


def build():
    return {k: [make_item(f, k, s) for f in FAMILIES for s in SEEDS] for k in RUNGS}


def extract(text):
    last = None
    for line in text.splitlines():
        t = line.strip().strip("*`").strip()
        if t.upper().startswith("ANSWER:"):
            last = t[7:].strip().strip("*`").strip()
    return last


def norm(s):
    return None if s is None else s.replace(" ", "").replace("'", "").replace("[", "").replace("]", "").lower()


def correct(text, answer):
    return norm(extract(text)) == norm(answer)


if __name__ == "__main__":
    data = build()
    print({k: len(v) for k, v in data.items()})
    print(json.dumps(data[3][0], indent=1))
