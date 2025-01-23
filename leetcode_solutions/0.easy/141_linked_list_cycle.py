import unittest
from typing import List, Optional

"""
Problem: https://leetcode.com/problems/valid-palindrome/description/
DATE: 5/01/25
TOPIC: string, Two Pointers

INPUTS:
-  string

CONSTRAINTS:
- All in lowercase letter
- without alphanumeric characters 
- 1 <= s.length <= 2 * 105
- s consists only of printable ASCII characters.

OUTPUTS:
- Return a boolean: true if the string is palindrome or False

EDGE CASES:
- string empty
- null value

TIME: 
O(n)

SPACE: 
O

NOTES:
- Case insensitive (uppercase/lowercase non importa)
- Solo caratteri alfanumerici contano
- Spazi e punteggiatura vengono ignorati

QUESTION: I -> INTERVIEWER - M -> Me

Non ho domande



MEMORIZE

PSEUDOCODE
uso two pointer opposite direction
l = 0 
r = len(s)-1
cancel no alphanumeric characters and transform the string in lower case

while l<r:
    se il s[l] != s[r]
        return false
return true



"""


# Reasoning


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: Optional[ListNode]) -> bool:
    # Prima verifichiamo se la lista è vuota o ha un solo elemento
    if not head and  not head.next:
        return False

    slow = fast = head #partono tutti e due dalla stessa pista

    while fast and fast.next: #se fast e fast.next sono null già dall'inizio allora non c'è ciclo
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False #se fast arriva alla fine non c'è ciclo


class UnitTest(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(hasCycle([3,2,0,-4]), True)  # have a cycle

    def test_case_1(self):

        self.assertEqual(hasCycle([3,2,0]), False)  # doesn't have a cycle

    def test_case_2(self):
        self.assertEqual(hasCycle("raceacar"), False)  # Not palindrome

    def test_case_3(self):
        self.assertEqual(hasCycle([]), True)  # Empty linked list

    def test_case_4(self):
        self.assertEqual(hasCycle(None), True)  # Null



if __name__ == "__main__":
    unittest.main()