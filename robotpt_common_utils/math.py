def round_down(x):
    if x >= 0:
        return int(x)
    if x < 0:
        return int(x) - 1


def bound(value, lower_bound=None, upper_bound=None):
    if upper_bound is not None and lower_bound is not None:
        if upper_bound < lower_bound:
            raise ValueError("Upper bound must be greater than lower bound")

    if upper_bound:
        value = min(value, upper_bound)
    if lower_bound:
        value = max(value, lower_bound)

    return value