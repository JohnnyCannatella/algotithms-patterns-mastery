#!/bin/python3
import os
import unittest
from typing import List

"""
Problem: https://leetcode.com/problems/assign-cookies/description/
DATE: 12/01/25
TOPIC: two pointer, sorting, array

INPUTS:
- g -> integer list (greed factor of the child)
- j -> integer list (size of cookie)

CONSTRAINTS:
1 <= g.length <= 3 * 104
0 <= s.length <= 3 * 104
1 <= g[i], s[j] <= 231 - 1

OUTPUTS:
- return an integer that represent the content children

EDGE CASES:
- empty array []
- g[1],s[1]
- none case

NOTES:
- If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content.

QUESTION: I -> INTERVIEWER - M -> Me
    M: if we have edge case like empty array or none, we return 0 or none ?
    I: 
    
TIME: 

SPACE:
 
PSEUDOCODE

"""

def findContentChildren(g: List[int], s: List[int]) -> int:
    if not g or not s:
        return 0
    g.sort()
    s.sort()
    child = cookie = 0
    content_child = 0

    while child<len(g) and cookie<len(s):
        if s[cookie] >= g[child]:
            content_child += 1
            child+= 1
            cookie += 1
        else:
            cookie += 1
    return content_child


class UnitTest(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(findContentChildren([10,9,8,7], [5,6,7,8]), 2)

if __name__ == "__main__":
    UnitTest()