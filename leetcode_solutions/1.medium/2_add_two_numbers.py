#!/bin/python3
import os
import unittest
from typing import List, Optional

"""
Problem: https://leetcode.com/problems/add-two-numbers/
DATE: 21/01/25
TOPIC:

INPUTS:
- l1 : linked list (non-empty and non-negative integers)
- l2 : linked list (non-empty and non-negative integers)

CONSTRAINTS:
0 <= Node.val <= 9
The number of nodes in each linked list is in the range [1, 100]
It is guaranteed that the list represents a number that does not have leading zeros.

OUTPUTS:
- the reverse linked list of the sum of l1 + l2

EDGE CASES:
- l1=[1] - l2[1] -> l3=[2]
- l1[0] - l2[0] -< l3[0]
- none
- l1 = [1,2,3] - l2= [9,9,9] -> caso in cui ci sono i riporti

NOTES:
- l1 and l2 is not empy so i can avoid this edge case
- if l1 and l2 is [0] return [0]

QUESTION: I -> INTERVIEWER - M -> Me

    I: examples ?
    M: l1 = [1,2,3] - l2= [5,6,7] -> Result = l3=[6801]
    
TIME: 

SPACE: 
 
PSEUDOCODE


"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    curr = dummy
    carry=0
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        sum = val1 + val2 + carry
        carry = sum // 10
        new_val = sum % 10

        curr.next = ListNode(new_val)
        curr = curr.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next


class UnitTest(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual()

    def test_example_case_2(self):
        self.assertEqual()

if __name__ == "__main__":
    UnitTest()