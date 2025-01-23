#!/bin/python3
import os
import unittest
from typing import Optional

"""
Problem: https://leetcode.com/problems/palindrome-linked-list/description/
DATE: 07/01/25
TOPIC: Linked list, Two Pointers, palindrome

INPUTS:
- single linked list

CONSTRAINTS:
- The number of nodes in the list is in the range [1, 105].
- 0 <= Node.val <= 9

OUTPUTS:
true or false in base of the linked list is a palindrom

EDGE CASES:
- empty list [] or none
- single number in the list [1]

TIME: 

SPACE: 
O(1) -> non ho bisogno di creare nuove strutture dati

NOTES:
- un palindromo in una linked list è strutturato in questo modo: [1,2,2,1]

QUESTION: I -> INTERVIEWER - M -> Me

    M: 
    I: 
    
PSEUDOCODE
def reverse(head):
    prev = None
    curr = head
    
    while curr:
        next_temp = curr.next  # Salva il prossimo nodo
        curr.next = prev       # Inverte il puntatore
        prev = curr           # Sposta prev
        curr = next_temp      # Sposta curr
    
    return prev              # prev sarà il nuovo head

def Solution()
p1 = p2 = head

#essendo una linked list non ho informazioni che avrei con un array, per cui escluderei l'utilizzo dell'opposite direction,
#mentre si potrebbe usare una same direction con two pointer.

while 

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse(head):
    prev = None
    curr = head

    while curr:
        next_temp = curr.next  # Salva il prossimo nodo
        curr.next = prev  # Inverte il puntatore
        prev = curr  # Sposta prev
        curr = next_temp  # Sposta curr

    return prev  # prev sarà il nuovo head


def isPalindrome(head: Optional[ListNode]) -> bool:
    # Edge case
    if not head or not head.next:
        return True

    # 1. Trova il punto medio usando slow/fast
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # 2. Inverti la seconda metà
    # slow è ora nel mezzo
    second_half = slow
    prev = None
    while second_half:
        next_temp = second_half.next
        second_half.next = prev
        prev = second_half
        second_half = next_temp

    # 3. Confronta le due metà
    first_half = head
    second_half = prev
    while second_half:  # la seconda metà sarà sempre più corta o uguale
        if first_half.val != second_half.val:
            return False
        first_half = first_half.next
        second_half = second_half.next

    return True


class UnitTest(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual()

    def test_example_case_2(self):
        self.assertEqual()

if __name__ == "__main__":
    UnitTest()