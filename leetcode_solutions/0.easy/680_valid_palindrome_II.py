#!/bin/python3
import os
import unittest
from typing import List

"""
Problem: https://leetcode.com/problems/valid-palindrome-ii/description/
DATE: 12/01/25
TOPIC: string, two pointer, opposite direction

INPUTS:
- s: string
CONSTRAINTS:
0<len(s)<10^4

OUTPUTS:
return true if the string is a palindrome

EDGE CASES:
- empty string
- none
- s -> "s"
- s -> "ss"

NOTES:
- can remove max one character

QUESTION: I -> INTERVIEWER - M -> Me
    M:if there is an empty string I have return false or I can consider it a palindrome ?
    I: Una stringa vuota è considerata palindroma, quindi return true
    
    M:the string can contain number ?
    I: La stringa contiene solo lettere minuscole a-z
    
    
TIME: 

SPACE:
 
PSEUDOCODE

"""


def validPalindrome(s: str) -> bool:
    def check_palindrome(s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            # Prova entrambe le possibilità:
            # 1. Rimuovi carattere a sinistra
            # 2. Rimuovi carattere a destra
            return check_palindrome(s, left + 1, right) or check_palindrome(s, left, right - 1)
        left += 1
        right -= 1

    return True


class UnitTest(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual()

    def test_example_case_2(self):
        self.assertEqual()

if __name__ == "__main__":
    UnitTest()