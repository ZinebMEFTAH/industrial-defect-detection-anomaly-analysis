"""Experiment protocol for 100%, 10%, 1%, and 0% labelled defects."""

LABEL_BUDGETS = (1.0, 0.10, 0.01, 0.0)
RANDOM_SEEDS = (42, 123, 2027)

def describe_protocol():
    return {
        "label_budgets": LABEL_BUDGETS,
        "random_seeds": RANDOM_SEEDS,
        "note": "Unsupervised models train on normal images only.",
    }
