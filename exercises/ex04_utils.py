"""EX04 - Exercise using 'List' Utility Functions."""

__author__ = "730563340"


def all(num_list, given_int) -> bool:
    """Check if all elements in num_list are equal to given_int."""
    num_idx: int = 0  # Initialize the index

    # Check if num_list is empty, return False.
    if len(num_list) == 0:
        return False

    while num_idx < len(num_list):
        if num_list[num_idx] != given_int:
            return False
        num_idx += 1

    return True


def max(input: list[int]) -> int:
    """Find the maximum integer in the input list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")

    max_num = input[0]  # Initialize max_num with the first element of the list
    num_idx = 1  # Begin comparison from the second element.

    while num_idx < len(input):
        if input[num_idx] > max_num:
            max_num = input[num_idx]
        num_idx += 1

    return max_num


def is_equal(list1, list2) -> bool:
    """Check if two lists of integers are equal at each index."""
    if len(list1) != len(list2):
        return False

    i: int = 0  # Initialize the index
    while i < len(list1):
        if list1[i] != list2[i]:
            return False
        i += 1

    return True
