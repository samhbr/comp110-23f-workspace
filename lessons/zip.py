"""Combining two lists into a dictionary"""

__author__ = "730563340"

def zip_function(str_list: list[int], int_list: list[int]) -> dict[str, int]:
    # Check if the input lists are of different lengths or empty
    if len(str_list) != len(int_list):
        return {}
    
    # Check if the input lists are empty
    if len(str_list) == 0:
        return {}
    
    # Create a dictionary with the keys from the first list and values from the second list
    result_dict = {str_list[i]: int_list[i] for i in range(len(str_list))}
    
    return result_dict
