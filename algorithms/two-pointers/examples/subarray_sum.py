#!/bin/python3
import os
import unittest
from typing import List

"""
Problem: https://algo.monster/problems/subarray_sum
DATE: 11/01/25
TOPIC: subarray, prefix_sum

INPUTS:
- nums: array of integer
- target: integer (

CONSTRAINTS:

OUTPUTS:
- subarray that sums to target and return the start and end indices of the subarray.

EDGE CASES:
- empty array []
- None
- target = 0 or = 1
- array with one value [1]


TIME: 

SPACE: 

NOTES:

QUESTION: I -> INTERVIEWER - M -> Me

    M:
    I: 
    
PSEUDOCODE

"""
#Input: arr: [1, -20, -3, 30, 5, 4] target: 7
def subarray_sum(arr: List[int], target: int) -> List[int]:
    if not arr:
        return [-1, -1]
    prefix_sum = {0: -1}
    current_sum = 0
    for i in range(len(arr)):
        current_sum += arr[i]
        # Se current_sum - target esiste nel dizionario,
        # abbiamo trovato un subarray con somma = target
        if current_sum - target in prefix_sum:
            start = prefix_sum[current_sum - target] + 1
            return [start, i +1]
        prefix_sum[current_sum] = i
    return [-1,-1]


class UnitTest(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual()

    def test_example_case_2(self):
        self.assertEqual()

if __name__ == "__main__":
    UnitTest()