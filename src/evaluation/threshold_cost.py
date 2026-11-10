def expected_cost(y_true, y_pred, false_negative_cost=10.0, false_positive_cost=1.0):
    """Cost for y_true/y_pred encoded as 1=defective, 0=normal."""
    if len(y_true) != len(y_pred):
        raise ValueError("y_true and y_pred must have the same length")
    fn = sum(t == 1 and p == 0 for t, p in zip(y_true, y_pred))
    fp = sum(t == 0 and p == 1 for t, p in zip(y_true, y_pred))
    return fn * false_negative_cost + fp * false_positive_cost
