import ladder_gen as g


def test_hand_worked_ledger():
    # A=10,B=5,C=0: move 8 A->B (A=2,B=13); move 9 A->C does nothing (A=2<9); move 4 B->C (B=9,C=4)
    bal = {"A": 10, "B": 5, "C": 0}
    for s, d, a in [("A", "B", 8), ("A", "C", 9), ("B", "C", 4)]:
        if bal[s] >= a:
            bal[s] -= a
            bal[d] += a
    assert bal == {"A": 2, "B": 9, "C": 4}


def test_extract_and_correct():
    assert g.extract("blah\nANSWER: A=1,B=2,C=3") == "A=1,B=2,C=3"
    assert g.correct("x\n**ANSWER: a=1, b=2, c=3**", "A=1,B=2,C=3")
    assert not g.correct("no answer line", "A=1,B=2,C=3")
    assert g.extract("ANSWER: 1\nANSWER: 2") == "2"


def test_deterministic_and_sized():
    a, b = g.build(), g.build()
    assert a == b
    assert all(len(v) == 15 for v in a.values())
    ids = [i["id"] for v in a.values() for i in v]
    assert len(ids) == len(set(ids)) == 90


def test_planted_perfect_and_broken_solvers_separate():
    data = g.build()
    # perfect solver = reads the answer field: must score 1.0 everywhere
    for items in data.values():
        assert all(g.correct("ANSWER: " + i["answer"], i["answer"]) for i in items)
    # planted broken solver: always answers 'ANSWER: 0' must score near 0 (control against a lenient scorer)
    hits = sum(g.correct("ANSWER: 0", i["answer"]) for items in data.values() for i in items)
    assert hits == 0


def test_answers_vary():
    data = g.build()
    for k, items in data.items():
        assert len({i["answer"] for i in items}) > 10
