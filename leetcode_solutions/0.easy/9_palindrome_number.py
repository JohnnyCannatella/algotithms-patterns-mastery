#!/bin/python3
import os
import unittest
from typing import List

"""
Problem: https://leetcode.com/problems/palindrome-number/
Difficulty: Easy
DATE: 23/01/25
TOPIC:
"""

"""
INPUTS:
- x: integer
OUTPUTS:
- return true if x is a palindrome
- else false
CONSTRAINTS:
-2^31 <= x <= 2^31 - 1
EDGE CASES:
- len(n) == 1 -> is a palindrome
- len(n) == 0 or == 1
- n is none
NOTES:
    
Complexity:
- Time: O(?)
- Space: O(?)
 
"""

"""

Approach:
1. left = 0, right = 4: confronto '1' con '1' ✓
2. left = 1, right = 3: confronto '2' con '2' ✓
3. left = 2, right = 2: il while termina
4. return True

"""

"""
QUESTION: I -> INTERVIEWER - M -> Me

    M:
    I: 
"""

def isPalindrome(x: int) -> bool:
        x = str(x)
        left = 0
        right = len(x)-1
        while left < right:
            if x[left] != x[right]:
                return False
            left+=1
            right-=1
        return True


class UnitTest(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual()

    def test_example_case_2(self):
        self.assertEqual()

if __name__ == "__main__":
    UnitTest()