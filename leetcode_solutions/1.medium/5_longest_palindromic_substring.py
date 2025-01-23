#!/bin/python3
import os
import unittest
from typing import List

"""
Problem: https://leetcode.com/problems/longest-palindromic-substring/
DATE: 23/01/25
TOPIC:Two Pointers, String, Dynamic Programming

INPUTS:
- s: string

CONSTRAINTS:
- 1 <= s.length <= 1000
- s consist of only digits and English letters.

OUTPUTS:
- max_substring: string that rappresent the longest palindromic substring 

EDGE CASES:
- s.length == 1 -> return 1
- s empty return 0
- s none return 0
- s equal character "aaaa"
- s.lenght == 2 "ab" -> is palindrom


EXAMPLES:
- "bacab" -> bac is valid substring and are palindromic

NOTES:
- in questo caso devo sia verificare il palindromo usando il two pointer che la substring usando hash table

QUESTION: I -> INTERVIEWER - M -> Me

    M: posso considerare empty string e none come ritorno 0
    I: 
    
     M: essendo che nei CONSTRAINTS è specificato questo 1 <= s.length <= 1000 -> vuol dire che quei edge case non devo considerarli ? nelle interview come dovrei comportarmi ?
    I: 
    
TIME: 
O(n)
SPACE:
Non ho bisogno di creare nuove strutture dati O(1)

PSEUDOCODE

max_sub = ""
if len(s) == 1: return s
for curr in range(1,len(s)):
    left = curr-1
    right = curr +1
    
    if s[left] == r[right] and left >= 0 and right < len(s):
        aggiungo i caratteri nella max_sub
        left-=1 #continuo ad allargare la finestra
        right+=1

return max_sub

while 

"""

def longestPalindrome(s: str) -> str:

    if len(s)< 2: return s
    start = 0
    max_len = 1

    def expand_around_center(left: int, right: int) -> None:
        nonlocal start, max_len

        while left >= 0 and right <len(s) and s[left] == s[right]:
            curr_len = left - right +1

            if curr_len > max_len:
                start = left
                max_len = curr_len
            left-=1
            right+=1

    for i in range(len(s)):
        expand_around_center(i, i)
        expand_around_center(i,i+1)

    return s[start:start+max_len]


class UnitTest(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual()

    def test_example_case_2(self):
        self.assertEqual()

if __name__ == "__main__":
    UnitTest()