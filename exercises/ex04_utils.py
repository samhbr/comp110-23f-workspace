""" EX04 - Exercise using 'List' Utility Functions"""

__author__ = "730563340"

from random import randint

def all(num_list: list[int], given_int: int) -> bool:
    if len(num_list) == 0:
        return False
    
    for num in num_list:
        if num != given_int:
            return False
    
    return True

def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    
    max_num = input[0]  # Initialize max_num with the first element of the list
    num_idx = 1  # Begin comparison from second element
    
    while num_idx < len(input):
        if input[num_idx] > max_num:
            max_num = input[num_idx]
        num_idx += 1
    
    return max_num

def is_equal(list1: list[int], list2: list[int]) -> bool:
    if len(list1) != len(list2):
        return False

    i = 0  # Initialize the index
    while i < len(list1):
        if list1[i] != list2[i]:
            return False
        i += 1
    return True