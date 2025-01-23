#!/bin/python3
import os
import unittest
from typing import List

"""
Problem: https://leetcode.com/problems/contains-duplicate-ii/description/
DATE: 20/01/25
TOPIC: Array, Hash Table, Sliding Window

INPUTS:
- nums: integer array
- k: integer

CONSTRAINTS:

OUTPUTS:
-  return true if array[num] === k and abs(i - j) <= k.

EDGE CASES:
- k > nums
- none

NOTES:
- These condition abs(i - j) <= k means that the duplicate should be before a distance k

QUESTION: I -> INTERVIEWER - M -> Me
    M:
    I: 
    
TIME: 

SPACE:
 
PSEUDOCODE
init window and sum = 0
left= 0
for right in range(len(nums)):
    append input to window
    while valid(window) and right <= k:
        verify the condition 
            return true
        remove input[left] from window
            left += 1 
    return false

"""

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    seen = {}
    for i, num in enumerate(nums):
        # Se abbiamo già visto questo numero
        if num in seen:
            # Verifichiamo la distanza dall'ultima volta
            if i - seen[num] <= k:
                return True
            # Aggiorniamo l'ultimo indice in cui abbiamo visto questo numero
            seen[num] = i

    return False


class UnitTest(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual()

    def test_example_case_2(self):
        self.assertEqual()

if __name__ == "__main__":
    UnitTest()