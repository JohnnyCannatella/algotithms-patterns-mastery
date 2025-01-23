#!/bin/python3
import os
import unittest
from collections import Counter
from typing import List

"""
Problem: https://algo.monster/problems/least_consecutive_cards_to_match
DATE: 11/01/25
TOPIC: Array, sliding window

INPUTS:
cards: list of integer

CONSTRAINTS:
0<= len(cards) <=10^6

OUTPUTS:
- the minimum number of cards that you need to pick up to make a pair
- if there aren't matching pairs return -1

EDGE CASES:
- Empty list []
- list with one value [1]
- None list
- None couple existent [2,3,4]
- [2,2,2,2]

TIME: 

SPACE: 
With don't need to creare new space -> O(1)

NOTES:
- if there aren't matching pairs return -1
- list of integer

QUESTION: I -> INTERVIEWER - M -> Me

    M: i didn't understand this things: if we a pair with 3 card and another pair is after 4 card, I need to return both or just the min ?
    I: 
    
PSEUDOCODE

"""
#cards = [3, 4, 2, 3, 4, 7]
def least_consecutive_cards_to_match(cards: list[int]) -> int:
    if not cards:
        return -1
    min_length = float('inf')
    seen = {}
    for end in range(len(cards)):
        current_card = cards[end] #window = 3
        if current_card in seen:
            # Abbiamo trovato una coppia
            window_size = end - seen[current_card] + 1
            min_length = min(min_length, window_size)

        seen[current_card] = end

    return min_length if min_length != float('inf') else -1

#other solution:
def least_consecutive_cards_to_match_v2(cards: List[int]) -> int:
    window: Counter[int] = Counter()
    shortest = len(cards) + 1
    left = 0
    for right in range(len(cards)):
        window[cards[right]] += 1
        while window[cards[right]] == 2:
            shortest = min(shortest, right - left + 1)
            window[cards[left]] -= 1
            left += 1
    return shortest if shortest != len(cards) + 1 else -1

class UnitTest(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual()

    def test_example_case_2(self):
        self.assertEqual()

if __name__ == "__main__":
    UnitTest()