#!/bin/python3
import os
import unittest
from typing import List

"""
Problem: https://leetcode.com/problems/count-binary-substrings/description/
DATE: 12/01/25
TOPIC: string, two pointers

INPUTS:
s : string of binary

CONSTRAINTS:
1 <= s.length <= 105
s[i] is either '0' or '1'.

OUTPUTS:
int: the number of times they occur.

EDGE CASES:

NOTES:

QUESTION: I -> INTERVIEWER - M -> Me

    M:
    I: 
    
TIME: 

SPACE:
 
PSEUDOCODE

"""

def countBinarySubstrings(s: str) -> int:
    # Your code here
    pass


class UnitTest(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(countBinarySubstrings("00110011"), 6)

    def test_example_case_2(self):
        self.assertEqual()

if __name__ == "__main__":
    UnitTest()