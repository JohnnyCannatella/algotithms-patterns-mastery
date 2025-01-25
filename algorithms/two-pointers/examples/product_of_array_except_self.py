#!/bin/python3
import os
import unittest
from typing import List

"""
Problem: 
Difficulty: Easy
DATE: 25/01/25
TOPIC: two-pass approach, prefix_sum
"""

"""
INPUTS:
- nums: integer array
OUTPUTS:
- answer: array that rappresent the product of all the element except nums[i]
CONSTRAINTS:
EDGE CASES:
- len(nums) < 1
- nums empty or none
- nums[0,1]
NOTES:
- To calculate the product I have to exclude nums[i]
    
Complexity:
- Time: O(n), where n is the length of the input array. We traverse the array twice: once for prefix product and once for suffix product.
- Space: O(1) because i don't need to create a new DS
 
"""

"""

Approach: (two-pass approach)
1. prepare the prefix product -> gli devo passare l'array forse meno nums[i] ? qua immagino che non posso applicare accumulate
2. calculate query 

"""

"""
QUESTION: I -> INTERVIEWER - M -> Me

    M:
    I: 
"""


def product_of_array_except_self(nums: List[int]) -> List[int]:
    n = len(nums)
    answer = [1] * n  # Inizializziamo l'array risultato con tutti 1

    # Primo passo: calcoliamo i prodotti da sinistra
    # answer[i] conterrà il prodotto di tutti gli elementi a sinistra di i
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    # Secondo passo: calcoliamo i prodotti da destra e li combiniamo
    # Moltiplichiamo ogni elemento per il prodotto di tutti gli elementi a destra
    postfix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= postfix
        postfix *= nums[i]

    return answer


class UnitTest(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(product_of_array_except_self([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_example_case_2(self):
        self.assertEqual()

if __name__ == "__main__":
    UnitTest()