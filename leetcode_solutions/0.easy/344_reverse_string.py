#!/bin/python3
import os
import unittest
from typing import List

"""
Problem: 
DATE: 07/01/25
TOPIC: String, Two Pointers

INPUTS:
- array of characters

CONSTRAINTS:
1 <= s.length <= 105
s[i] is a printable ascii character.

OUTPUTS:
- reverse the array of characters

EDGE CASES:
- [] empty array
- [a] single character array
- None
- [0, 1] integer array

TIME: 

SPACE: 
O(1) we don't need to create new data stracture

NOTES:
- modify the input in-place

QUESTION: I -> INTERVIEWER - M -> Me

    M:
    I: 
    
PSEUDOCODE

two pointer opposite direction
left = 0
right = len(s)-1

while l<r:
    switch s[left] with s[right]
    l+=1
    r-=1

"""

def reverseString(s: List[str]) -> None:
    l = 0
    r = len(s)-1
    while l<r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1


class UnitTest(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual()

    def test_example_case_2(self):
        self.assertEqual()

if __name__ == "__main__":
    UnitTest()