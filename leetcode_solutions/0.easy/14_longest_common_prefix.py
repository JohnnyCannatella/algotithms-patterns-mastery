#!/bin/python3
import os
import unittest
from typing import List

"""
Problem: https://leetcode.com/problems/longest-common-prefix/
DATE: 22/01/25
TOPIC:

INPUTS:
- strs: array of string

CONSTRAINTS:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.

OUTPUTS:
- log_prefix: string that rappresent the common prefix string 
- "" if no common prefix

EDGE CASES:
- empty array
- ["s","s","s"]

NOTES:

QUESTION: I -> INTERVIEWER - M -> Me
    M: I have consider Upper and lowecase ? or i'll receive all the str just in one case ?
    I: See the constrain
    
TIME: 
Per l'approccio orizzontale:
O(S) dove S è la somma delle lunghezze di tutte le stringhe

Per l'approccio verticale:
O(m*n) dove:
m è la lunghezza della stringa più corta
n è il numero di stringhe nell'array

SPACE:
O(1) perché:
- Stiamo solo memorizzando il prefisso
- Non creiamo strutture dati aggiuntive che crescono con l'input
- Lo spazio utilizzato è costante indipendentemente dall'input
 
PSEUDOCODE

"""
#Orizzontal way
def longestCommonPrefix(strs: List[str]) -> str:
    prefix = strs[0]
    for str in strs[1:]:
        while str.startswith(prefix) == False:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

#Vertical way
def longestCommonPrefix(strs: List[str]) -> str:
    if not strs: return ""
    for i in range(len(strs[0])):  # per ogni carattere della prima stringa
        c = strs[0][i]  # prendi il carattere
        for str in strs[1:]:  # controlla tutte le altre stringhe
            if i >= len(str) or str[i] != c:
                return strs[0][:i]
    return ""


class UnitTest(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual()

    def test_example_case_2(self):
        self.assertEqual()

if __name__ == "__main__":
    UnitTest()