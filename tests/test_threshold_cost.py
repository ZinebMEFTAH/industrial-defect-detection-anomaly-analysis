from src.evaluation.threshold_cost import expected_cost

def test_expected_cost_counts_false_negative_and_false_positive():
    assert expected_cost([1, 0, 0], [0, 1, 0], 10, 1) == 11
