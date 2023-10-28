"""Testing my summation function."""

from sum_evens import sums_evens_in_list


def test_empty_sum() -> None: 
    """sum_events_in_list of empty list should be 0."""
    assert sums_evens_in_list([0]) == 0


def test_list_length_1():
    """Testing on a list with one element."""
    test_list: list[int] = [2]
    assert sums_evens_in_list(test_list) == 2 


def test_list_positives(): 
    """Testing sum on a list of positive integers."""
    test_list: list[int] = [1,2,3,4]
    assert sums_evens_in_list(test_list) == 6


def test_lists_negs_and_pos():
    """Testing sum of negatives and positives."""
    test_list: list[int] = [1,-2,3,4]
    assert sums_evens_in_list(test_list)
