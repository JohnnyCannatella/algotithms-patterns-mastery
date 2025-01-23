#!/bin/python3
import os
import unittest
from typing import List

"""
Problem: https://leetcode.com/problems/reverse-vowels-of-a-string/description/
DATE: 08/01/25
TOPIC: String, Two Pointers

INPUTS:
- string 

CONSTRAINTS:
1 <= s.length <= 3 * 105
s consist of printable ASCII characters.

OUTPUTS:
- reverse only the vowels in the string

EDGE CASES:
- empty string ""
- single character string -> s
- None
- string without vowels -> str

TIME: 

SPACE: 
O(1) we don't need to create new data stracture

NOTES:
- The vowels are 'a', 'e', 'i', 'o', and 'u'

QUESTION: I -> INTERVIEWER - M -> Me

    M:
    I: 
    
PSEUDOCODE (First solution) Not complete

vowels = ['a', 'e', 'i', 'o', 'u']

two pointer opposite direction
l = 0
r = len(s)-1

while l<r:
    if s[l] in vowels and s[r] in vowels :
        switch s[l] with s[r]
        l+=1
        r-=1
    else if s[l] in vowels:
        r-=1
    else:
        l+=1

"""

def reverseVowels(s: str) -> str:
    vowels = set('aeiouAEIOU')
    s = list(s)
    l = 0
    r = len(s)-1
    while l<r:
        if s[l] in vowels and s[r] in vowels:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        elif s[l] in vowels:
            r -= 1
        else:
            l += 1
    return ''.join(s)

class UnitTest(unittest.TestCase):
    def test_example_case(self):
        self.reverseVowels(("IceCreAm"), "AceCreIm") #normal case

    def test_example_case_2(self):
        self.reverseVowels(("str"), "str") #edge case string without vowels

    def test_example_case_3(self):
        self.reverseVowels((None), None) #edge case none

    def test_example_case_4(self):
        self.reverseVowels((""), "") #edge case string empty

if __name__ == "__main__":
    UnitTest()