#!/bin/python3
import os
import unittest
from typing import List

"""
Problem: https://leetcode.com/problems/add-two-numbers/
DATE: 21/01/25
TOPIC: hash map, python basic

INPUTS:
- nums: integer
- target: integer

CONSTRAINTS:

OUTPUTS:
- an array with indices of the two nums that add up to target

EDGE CASES:
- target = 0
- none
- empy array

NOTES:
- this solution have one result
- we can't use the same element twice

QUESTION: I -> INTERVIEWER - M -> Me
    M:
    I: 
    
TIME: 

SPACE:
 
PSEUDOCODE

"""

def twoSum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


class UnitTest(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(twoSum([2,7,11,15], 9), [0,1])

    def test_example_case_2(self):
        self.assertEqual(twoSum([3,2,4], 6), [1,2])

if __name__ == "__main__":
    UnitTest()