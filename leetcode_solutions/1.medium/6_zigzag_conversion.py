#!/bin/python3
import os
import unittest
from typing import List

"""
Problem: https://leetcode.com/problems/zigzag-conversion/description/
Difficulty: Medium
DATE: 24/01/25
TOPIC:
"""

"""
INPUTS:
- s: string word to convert in a zigzag way
- numRows: number of raw
OUTPUTS:
- word: string converted in zigzag way
CONSTRAINTS:
- 1 <= s.length <= 1000
- s consists of English letters (lower-case and upper-case), ',' and '.'.
- 1 <= numRows <= 1000
EDGE CASES:
- empty string
- len(s) == 1
- numRows == 0 
- none value
- numRows > len(s)
NOTES:
- I have notice a pattern for example: 
    - PAYPALISHIRING -> numRows: 3 -> 1 value in the middle every two column 
    - PAYPALISHIRING -> numRows: 4 -> 2 value in the middle every two column
    - PAYPALISHIRING -> numRows: 5 -> 2 value in the middle every two column
    - PAYPALISHIRING -> numRows: 6 -> 3 value in the middle every two column 
    it's like the value in the middle rispect the rule numRows / 2 with pair numeber is correct

Complexity:
- Time: O(n) 
- Space: O(n) because we are memorize the char on the dictionary
 
"""

"""

Approach: WRONG
ho pensato all'utilizzo di due cicli e l'uso di un dict per tenere traccia della riga e dei caratteri: (anche se penso non sia la soluzione ottimale)
1. primo ciclo tengo il conteggio delle righe processate for i in numRows
2. secondo ciclo aggiungo effettivamente i caratteri al dict -> for c in range(len(s:numRows):
3. dentro il secondo ciclo aggiungo al riferimento di ogni riga i il carattere nel dict
4. mi estraggo i dati dal dict per formare una stringa oppure penso ci sia un metodo piu veloce per farlo

Così facendo la logica di sistemazione delle lettere e corretta peccato che manca l'applicazione della logica a zigzag.
Posso si usare direction per sapere quando andare su o giu e devo farlo So che lo zigzag dipende da numRows/2, ma come memorizzo questo discorso nel dict ?
"""

"""
QUESTION: I -> INTERVIEWER - M -> Me

    M:
    I: 
"""


def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    rows = {i: [] for i in range(numRows)}
    current_row = 0
    direction = 1
    for char in s:
        rows[current_row].append(char)

        if current_row == 0:
            direction = 1
        elif current_row == numRows -1:
            direction = -1
        current_row += direction

    result = ''
    for i in range(numRows):
        result += ''.join(rows[i])

    return result


class UnitTest(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual()

    def test_example_case_2(self):
        self.assertEqual()

if __name__ == "__main__":
    UnitTest()