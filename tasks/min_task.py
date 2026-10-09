# %%
import kaggle_benchmarks as kbench

# %%
@kbench.task(name="ceiling-min")
def ceiling_min(llm):
    response = llm.prompt("What is 2 + 2?")
    kbench.assertions.assert_in("4", response, expectation="Should contain 4")

ceiling_min.run(kbench.llm)
