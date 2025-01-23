import unittest
from typing import List

"""
Problem: https://leetcode.com/problems/merge-sorted-array/description/
DATE: 5/01/25
TOPIC: Array, Two Pointers, Sorting

INPUTS:
– Two integer arrays nums1 and nums2
- two integers m and n (number of elements)

CONSTRAINTS:
nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109

OUTPUTS:
- Single array sorted in non-decreasing order.

EDGE CASES:
m or n = -1

TIME: 
È O(n + m) perché:
- Il primo while loop scorre una volta attraverso entrambi gli array
- Il secondo while loop potrebbe scorrere gli elementi rimanenti di nums2
- In totale, ogni elemento viene processato una sola volta

SPACE: 
O(1) perché:
- Stiamo usando solo tre puntatori (p, p1, p2)
- Non stiamo creando nessuna struttura dati aggiuntiva
- Stiamo modificando l'array in-place

NOTES:
- sorted in non-decreasing order
- Non return array by the function but use nums1.

QUESTION: I -> INTERVIEWER - M -> Me

    M: Could you explain your understanding of this problem in your own words? 
    I: I have two array in non-decrease order that I have to merge in place on nums1
    
    M:What are some example inputs and outputs that could help us understand the problem better?
    I: [1,2,3] m=2, [2,4,6] n= 3 -> Output: [1,2,2,4,6]
    
    M:Before thinking about the solution, what are some constraints or edge cases we should consider?
    I: see above
    
    M: What's your initial thought about the space complexity requirements, given that we need to store the result in nums1?
    I: O(m+n)
    
MEMORIZE
- "Riempi dal fondo" - parti dalla fine perché hai spazio libero
- "Prendi il più grande" - ad ogni passo, scegli il numero più grande tra i due array
- "Pulisci gli avanzi" - alla fine, copia eventuali numeri rimasti in nums2
    
"""

#Reasoning


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1
    while p1 >= 0 and p2 >= 0:
        if nums2[p2] >= nums1[p1]:
            nums1[p] = nums2[p2]
            p2 -= 1
        else:
            nums1[p] = nums1[p1]
            p1 -= 1
        p -= 1
    while p2>= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1

class UnitTest(unittest.TestCase):
    def test_example_case_0(self):
        self.assertEqual(merge([0], 0, [1], 1), [1])

    def test_example_case(self):
        self.assertEqual(merge([1,2,3,0,0,0], 3, [2,5,6], 3), [1,2,2,3,5,6])

    def test_example_case_2(self):
        self.assertEqual(merge([1], 1, [], 0), [1])

if __name__ == "__main__":
    UnitTest()