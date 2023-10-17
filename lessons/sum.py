"""Summing the elements of a list using different loops!"""
__author__ = "730563340"


def w_sum(vals: list[float]) -> float:
    """Sum using a while loop."""
    idx: int = 0
    total_sum: float = 0.0
    while idx < len(vals):
        total_sum += vals[idx]
        idx += 1
    return total_sum


def f_sum(vals: list[float]) -> float:
    """Sum using a for loop."""
    total_sum: float = 0.0
    for elem in vals:
        total_sum += elem
    return total_sum


def f_range_sum(vals: list[float]) -> float:
    """Sum using a for loop with range."""
    total_sum: float = 0.0
    for idx in range(0, len(vals)):
        total_sum += vals[idx]
    return total_sum