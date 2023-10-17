"""Summing the elements of a list using different loops!"""
__author__ = "730563340"

def w_sum(vals: list[float]) -> float: 
    idx: int = 0
    sum: float = 0.0
    while idx < len(vals): 
        sum += w_sum[idx]
        idx += 1 
    return sum 

def f_sum(vals: list[float]) -> float: 
    sum: float = 0.0 
    for elem in vals:
        sum += elem  
    return sum 

def f_range_sum(vals: list[float]) -> float: 
    sum: float = 0.0
    for idx in range (0,len(f_range_sum)):
        sum += vals[idx]
    return sum 