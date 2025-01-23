import unittest
from typing import List, Optional

"""
Problem: https://leetcode.com/problems/intersection-of-two-linked-lists/description/
DATE: 6/01/25
TOPIC: Hash Table, Linked List, Two Pointers

INPUTS:
-  linked-lists headA
-  linked-lists headB

CONSTRAINTS:
The number of nodes of listA is in the m.
The number of nodes of listB is in the n.
1 <= m, n <= 3 * 104
1 <= Node.val <= 105
0 <= skipA <= m
0 <= skipB <= n
intersectVal is 0 if listA and listB do not intersect.
intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.

OUTPUTS:
- return the node at which the two lists intersect.
- else return null

EDGE CASES:
- Head null or empty
- Heads with one number

TIME: 


SPACE: 
O(1)

NOTES:
- there are no cycles anywhere in the entire linked structure.
- the linked lists must retain their original structure

QUESTION: I -> INTERVIEWER - M -> Me


PSEUDOCODE
uso two pointer same direction
p1 = 0 
p2= len(s)-1
#Gestisco le due liste null, empty e se entrambe hanno un solo valore

while p1 != null And p2 != null:
    #se il nodo di head1 si trova allo stesso posto di head2
        return nodo di intersezione
    
    #se head1 finisce prima di head2
        fai ri-iniziare il p1 da head2
    #se head2 finisce prima di head1
        fai ri-iniziare il p2 da head1
    
return null



"""


# Reasoning


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    if not headA or not headB:
        return None

    p1 = headA
    p2 = headB

    while p1 != p2:
        p1 = headB if p1 is None else p1.next
        p2 = headA if p2 is None else p2.next

    return p1


class UnitTest(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(getIntersectionNode([3,2,0,-4], [3,2,0,-4]), -4)  # have intersection

    def test_case_1(self):

        self.assertEqual(getIntersectionNode([3,2,0], [1,2,5,6]), None)  # doesn't have intersection

    def test_case_2(self):
        self.assertEqual(getIntersectionNode([], []), False)  # Empty linked list

    def test_case_3(self):
        self.assertEqual(getIntersectionNode(None, [3,2,0]), True)  # Empty linked list


if __name__ == "__main__":
    unittest.main()