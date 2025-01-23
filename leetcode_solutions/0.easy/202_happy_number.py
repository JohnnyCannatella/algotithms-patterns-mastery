import unittest
from typing import List, Optional

"""
Problem: https://leetcode.com/problems/happy-number/
DATE: 6/01/25
TOPIC: Hash Table, Math, Two Pointers

INPUTS:
Integer number

CONSTRAINTS:
1 <= n <= 231 - 1

OUTPUTS:
Return true if the number is a happy number
else false

EDGE CASES:
- n <= 0 (non valido per definizione, devono essere numeri positivi)
- n = 1 (caso base, è un happy number)
- empty/None

TIME: 

SPACE: 
O(1)

NOTES:
happy number è il risultato della divisione del numero a decimale splitato e sommato le cifre per le sue cifre come 10 -> 1+0

QUESTION: I -> INTERVIEWER - M -> Me


PSEUDOCODE
slow = fast = 0
while s != f:
    n = sum_squares(n)
    if n == 1 return true
    slow+=1
    fast+=2
    
return false

"""


def isHappy(self, n: int) -> bool:
    def sum_squares(num):
        total = 0
        while num > 0:
            digit = num % 10
            total += digit * digit
            num = num // 10
        return total

    slow = n
    fast = n

    while True:
        slow = sum_squares(slow)  # un passo
        fast = sum_squares(sum_squares(fast))  # due passi

        if fast == 1:  # abbiamo trovato 1, è happy
            return True
        if slow == fast:  # abbiamo trovato un ciclo
            return False


class UnitTest(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(isHappy(1), True)  #

    def test_case_1(self):

        self.assertEqual(isHappy(3), False)  #

    def test_case_2(self):
        self.assertEqual(isHappy(4), False)  #

    def test_case_3(self):
        self.assertEqual(isHappy(-1), True)  #


if __name__ == "__main__":
    unittest.main()