#!/bin/python3
import os
import unittest
from typing import List

"""
Problem: https://algo.monster/problems/find_all_anagrams
DATE: 10/01/25
TOPIC: Sliding window, string

INPUTS:
- original: string
- check: string 

CONSTRAINTS:
- 1 <= len(original), len(check) <= 10^5
- solo caratteri minuscoli inglesi

OUTPUTS:
- starting index (in asc way) of all substring where the anagram starting

EDGE CASES:
- empty string
- None
- original: test - check: test
- original: test - check: ""
- check more longer then original

TIME: 

SPACE:
We have to create a new structures

NOTES:
- the output must be sorted in ascending order

QUESTION: I -> INTERVIEWER - M -> Me
    M:
    I: 
    
PSEUDOCODE - Sliding window
#usare una finestra di dimensione check
window = len(check)
index = []

#Mantenere un conteggio dei caratteri nella finestra
start = 0

for end in range(window, len(original)):
    #devo confrontare original[end] == original[:window] 
        se true aggiungo ad un array -> index.append(end=  


"""


def findAnagrams(original, check):
    # Crea il conteggio dei caratteri di check
    check_count = {}  # dizionario per contare i caratteri in check
    for c in check:
        check_count[c] = check_count.get(c, 0) + 1

    # Inizializza la finestra
    window_count = {}  # dizionario per la finestra corrente
    result = []
    window = len(check)

    # Inizializza la prima finestra
    for i in range(window):
        c = original[i]
        window_count[c] = window_count.get(c, 0) + 1

    # Se la prima finestra è un anagramma
    if window_count == check_count:
        result.append(0)

    # Scorri la finestra
    for end in range(window, len(original)):
        # Aggiungi nuovo carattere
        window_count[original[end]] = window_count.get(original[end], 0) + 1

        # Rimuovi carattere che esce dalla finestra
        start_char = original[end - window]
        window_count[start_char] -= 1
        if window_count[start_char] == 0:
            del window_count[start_char]

        # Controlla se è un anagramma
        if window_count == check_count:
            result.append(end - window + 1)

    return result


class UnitTest(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual()

    def test_example_case_2(self):
        self.assertEqual()

if __name__ == "__main__":
    UnitTest()