#!/bin/python3
import os
import unittest
from typing import List

"""
Problem: https://leetcode.com/problems/move-zeroes/
DATE: 07/01/25
TOPIC: Array, Two Pointers

INPUTS:
- integer array
CONSTRAINTS:

OUTPUTS:
-  the same array with 0 moved to the end

EDGE CASES:
- Empty array []
- None
- Array without Zero [1,2,3]
- Array with [0]

TIME:


SPACE: 
O(1) non ci sono nuove strutture dati

NOTES:
- do it in-place

PSEUDOCODE
Two pointer same direction
p1 = 0

for p2 in range(len(nums)):
    if nums[p2] != 0:
        Faccio lo switch
        p1+= 1

QUESTION: I -> INTERVIEWER - M -> Me

    M: Can I have manage the edge case ?
    I: 

"""

def moveZeroes(self, nums: List[int]) -> None:
    p1 = 0
    for p2 in range(len(nums)):
        if nums[p2] != 0:
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p1+=1


class UnitTest(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(moveZeroes([1,2,3,4]), None)

    def test_example_case_2(self):
        self.assertEqual(moveZeroes([1,2,3,4]), None)

if __name__ == "__main__":
    UnitTest()