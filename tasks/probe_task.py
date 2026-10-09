# %%
import kaggle_benchmarks as kbench

# %%
@kbench.task(name="ceiling-probe-two")
def ceiling_probe(llm) -> bool:
    response = llm.prompt("Reply with only the number: what is 17 * 3?")
    return "51" in response

ceiling_probe.run(kbench.llm)
