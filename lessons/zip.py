"""Combining two lists into a dictionary."""

__author__ = "730563340"


def zip(key_list: list[str], value_list: list[int]) -> dict[str, int]:
    """Creates a dictionary where the keys are the items of the first list and the values are the corresponding items at the same index of the second list."""
    #Check if the input lists are of different lengths or empty
    if (len(key_list) != len(value_list)) or (len(key_list) == 0):
        return {}
    zip: dict[str, int] = {}
    i: int = 0
    while i < len(key_list):
        zip[key_list[i]] = value_list[i]
        i += 1 
        return zip
