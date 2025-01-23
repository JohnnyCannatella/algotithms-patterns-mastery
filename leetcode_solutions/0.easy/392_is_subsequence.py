#!/bin/python3
import os
import unittest

"""
Problem: https://leetcode.com/problems/is-subsequence/
DATE: 11/01/25
TOPIC: Array, Two Pointers

INPUTS:
s: string
t: string
 
CONSTRAINTS:
0< len(s) and len(t) <= 10^6
s and t consist only of lowercase English letters.

OUTPUTS:
- return true if s in a subsequence of t
- else false

EDGE CASES:
- string empty
- duplicate string
- none
- len(string) > 1

TIME: 

SPACE:
O(1)

NOTES:

QUESTION: I -> INTERVIEWER - M -> Me
    M:
    I: 
    
PSEUDOCODE


"""

def isSubsequence(s: str, t: str) -> bool:
    if s == "":
        return True
    p1=p2=0
    while p2<len(t):
        if s[p1] == t[p2]:
            p1 += 1
            if p1 == len(s):
                return True
        p2+=1
    return False


class UnitTest(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual()

    def test_example_case_2(self):
        self.assertEqual()

if __name__ == "__main__":
    UnitTest()