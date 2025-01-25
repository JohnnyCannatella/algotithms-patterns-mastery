#!/bin/python3
import os
import unittest
from itertools import accumulate
from typing import List

"""
Problem: 
Difficulty: Easy/Medium/Hard
DATE: /01/25
TOPIC:
"""

"""
INPUTS:
- nums: integer array
OUTPUTS:
- sum : integer that represent sum of element between indices left and right
CONSTRAINTS:
- 0 < len(nums) < 10^6
- nums contain positive numbers

EDGE CASES:
- left or right out of range
- left > right
- len(nums) == 0
- nums[1] -> return nums[0]
- none 

NOTES:
- required to preprocess the array so that each query can be answered in constant time

Preprocessing (pre-elaborazione): è come creare un indice all'inizio del libro. Richiede tempo iniziale, ma poi rende le ricerche più veloci.

Nel nostro caso: è quello che facciamo UNA VOLTA quando riceviamo l'array iniziale
Esempio pratico: creare un array di somme prefisse
Query Time (tempo di risposta): è il tempo che ci vuole per trovare la risposta a ogni singola richiesta
Nel nostro caso: il tempo per calcolare la somma tra left e right
Esempio: se abbiamo le somme prefisse, possiamo rispondere in O(1)

Fast Preprocessing vs Fast Queries
Se dobbiamo fare MOLTE query sullo stesso array, è meglio:

Spendere più tempo all'inizio (preprocessing più lento)
Per avere risposte istantanee dopo (query velocissime)

Complexity:
- Time: O(?) -> devo fare n volte la somma per tutto l'array
- Space: O(1) i don't need to creare new DS
 
"""

"""
Approach:
1. Initialize the prefix sum array with the same length as the input array.
2. Calculate the prefix sum array:
    - First element is the same as the first element of the input array.
    - For subsequent elements, add the current element to the previous prefix sum.
3.For each query, return the difference between prefix sums at right and left - 1 indices.
"""

"""
QUESTION: I -> INTERVIEWER - M -> Me

    I -> Some questions to consider as you analyze:
        - What's the difference between preprocessing time and query time?
        - If we need to do multiple queries, what would be more important - fast preprocessing or fast queries?
        - What happens if we query the same range multiple times?
    M: I dunno
    
    M:"Prima di procedere, vorrei chiedere se posso utilizzare la funzione accumulate 
        di itertools per il prefix sum, o preferisce che implementi l'algoritmo manualmente?"
    I: 
    
    Se l'intervistatore non conosce accumulate, puoi dire:
    M:"accumulate è una funzione di Python che implementa efficientemente il pattern 
    del prefix sum. Posso mostrarle entrambe le implementazioni se preferisce."
"""

#Prefix sum application to array
def nums_array (nums: List[int]) -> List[int]:
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)
    return prefix

#evolution of prefix sum
def init_sum_array(nums: List[int]) -> List[int]:
    return list(accumulate(nums, initial=0))


def range_sum_query_immutable(nums: List[int], left: int, right: int) -> int:
    prefix = nums_array(nums)
    return prefix[right + 1] - prefix[left]


class UnitTest(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual()

    def test_example_case_2(self):
        self.assertEqual()

if __name__ == "__main__":
    UnitTest()