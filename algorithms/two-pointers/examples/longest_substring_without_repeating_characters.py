#!/bin/python3
import os
import unittest
from collections import defaultdict
from typing import List, Dict

"""
Problem: https://algo.monster/problems/longest_substring_without_repeating_characters
DATE: 10/01/25
TOPIC: sliding window, set, string
RELETED PATTERN: Brute force

INPUTS:
- string

CONSTRAINTS:
- 0 < len(s) < 10^2

OUTPUTS:
-  integer: max lenght of substring

EDGE CASES:
- empty string
- None
- string with all the element duplicate "aaaaaa" -> return 1
- all the elemente different "abcd" -> return 4

TIME: 

SPACE:

NOTES:
- La finestra è di dimensione variabile
- non bisogna considerare i doppioni

QUESTION: I -> INTERVIEWER - M -> Me
    M:
    I: 

"""

#string = abccabcabcc
def longest_substring_without_repeating_characters(s: str) -> int:
    start = 0
    window = set()
    lenght = 0
    for end in range(len(s)): #right = 0 in range (11)
        #s[right] = a
        while s[end] in window: #0 in []
            window.remove(s[start])
            start+=1

        window.add(s[end]) #window_sub[a]
        lenght = max(lenght, end - start + 1)
    return lenght

#other solution:
def longest_substring_without_repeating_characters_2(s: str) -> int:
    longest = 0
    l = 0
    counter: Dict[str, int] = defaultdict(int)
    for r in range(len(s)):
        counter[s[r]] += 1
        while counter[s[r]] > 1:
            counter[s[l]] -= 1
            l += 1
        longest = max(longest, r - l + 1)
    return longest


class UnitTest(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(longest_substring_without_repeating_characters("abccabcabcc"), 3) #normal case

    def test_example_case_2(self):
        self.assertEqual(longest_substring_without_repeating_characters("aaaabaaa"), 2)  # normal case

if __name__ == "__main__":
    UnitTest()