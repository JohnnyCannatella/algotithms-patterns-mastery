#!/bin/python3
import os
import unittest
from typing import List

"""
Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
DATE: 23/01/25
TOPIC: Hash Table, String, Sliding Window

INPUTS:
- s: string

CONSTRAINTS:
0 < s.length < 5 * 10^4
s consists of English letters, digits, symbols and spaces.

OUTPUTS:
- integer: max length of the longest substring

EDGE CASES:
- s -> empty
- s -> none
- s = "s"

NOTES:
- substring: caratteri contingui non doppi

QUESTION: I -> INTERVIEWER - M -> Me

    M: in base a cosa viene individuata una substring ? esempio: "abcabd" ->  substring = "abc" - ma nel caso di "pwwkew" -> perchè la substring è "wke" e non "kew"
    I: 

TIME: 
Devo verificare per ogni carattere la sua lunghezza
SPACE:
O(1) -> non devo creare strutture dati

PSEUDOCODE
left = right = 0
length = 0
seen = {} #Posso usare un dict per contare quante volte una lettere è spuntata e poi lo resetto

while left < len(s):
    mentre right < len(s) e finchè un carattere nel dict non è contenenuto piu volte (right in seen{})
        right += 1 # continuo ad aumentare finche non esce dal cliclo perchè non è piu una substring
        #memorizzo il carattere nel dict con il suo indice
    
    left+=1    
    #conteggio il max tra lenght e right + 1 perchè devo contare il carattere di left
return length
        

"""


def lengthOfLongestSubstring(s: str) -> int:
    left = right = 0
    max_lenght = 0
    seen = {}
    while left < len(s):

        if s[right] in seen and seen[s[right]] >= left:
            left = seen[s[right]] + 1
        seen[s[right]] = right
        current_lenght = right - left +1
        max_lenght = max(max_lenght, current_lenght)
        right +=1

    return max_lenght


class UnitTest(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual()

    def test_example_case_2(self):
        self.assertEqual()


if __name__ == "__main__":
    UnitTest()