#!/bin/python3
import os
import unittest
from typing import List

"""
Problem: https://leetcode.com/problems/valid-word-abbreviation/description/
DATE: 11/01/25
TOPIC: string, string matching, two pointer

INPUTS:
- word: string
- abbreviation: string

CONSTRAINTS:
1 <= word.length <= 20
word consists of only lowercase English letters.
1 <= abbr.length <= 10
abbr consists of lowercase English letters and digits.
All the integers in abbr will fit in a 32-bit integer.

OUTPUTS:
- return true if the word matches the abbreviation
- else false

EDGE CASES:
- empty string
- none
- word with 1 character
- abbreviation 

NOTES:
- any number of non-adjacent, non-empty substrings with their lengths

QUESTION: I -> INTERVIEWER - M -> Me
    M:
    I: 
    
PSEUDOCODE

TIME: 

SPACE: 

"""


def validWordAbbreviation(word: str, abbr: str) -> bool:
    i = j = 0  # i per word, j per abbr

    while i < len(word) and j < len(abbr):
        # Se troviamo una cifra
        if abbr[j].isdigit():
            # Leading zero non è permesso
            if abbr[j] == '0':
                return False

            # Costruiamo il numero completo
            num = 0
            while j < len(abbr) and abbr[j].isdigit():
                num = num * 10 + int(abbr[j])
                j += 1

            # Avanziamo nella parola del numero di posizioni
            i += num
        # Se troviamo una lettera
        else:
            if i >= len(word) or word[i] != abbr[j]:
                return False
            i += 1
            j += 1

    # Verifichiamo di aver consumato entrambe le stringhe
    return i == len(word) and j == len(abbr)


class UnitTest(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(validWordAbbreviation("internationalization", "i12iz4n"), True)

    def test_example_case_2(self):
        self.assertEqual()

if __name__ == "__main__":
    UnitTest()