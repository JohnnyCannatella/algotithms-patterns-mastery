#!/bin/python3
import os
import unittest
from typing import List

"""
Problem: https://leetcode.com/problems/valid-parentheses/description/
Difficulty: Easy
DATE: 25/01/25
TOPIC: two
"""

"""
INPUTS:
- s: string (contain just Parentheses)
OUTPUTS:
- true/false -> Valid input complying with the rules
NOTES:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.
Complexity:
- Time: O(?) 
- Space: O(1) -> We don't need to create new DS
 
"""

"""
QUESTION: I -> INTERVIEWER - M -> Me

    M:
    I: 
"""

"""
# REACTO Analysis:
# R - Repeat
# E - Examples
    1. "()" -> valid
    2. "(]" - not valid open/close brackets
    3. [()] - not valid order
    Edge cases:
    1. "" -> not valid empty case
    2. "[()" -> not valid miss closed brackets
    3. none -> not valid there isn't value
    4. "[" -> not valid just a character
# A - Approach
We can solve it with :
1. Two pointer pattern ->
    - set two pointer in same direction
    - We can evaluate that if len(s) == 1 or none or empty -> return false
    - I need to see every character in the string to validate the input
    - We have to use a cycle like -> for cycle to see every characters into the array
    - into the cycle with the pointer we can see if s[p1]
I think that this problem it's not walkable with two pointer but is better to use sliding windows but i'm not sure
# C - Code
# T - Test
# O - Optimize
"""


def solution():
    # Your code here
    pass


class UnitTest(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual()

    def test_example_case_2(self):
        self.assertEqual()

if __name__ == "__main__":
    UnitTest()