#EXAMPLE - TWO POINTERS -> Same Direction
#!/bin/python3

# EXCERCISE
"""
    Problem:
        Find the middle node of a linked list.
    INPUTS:
    - Type: Array of number: 0 1 2 3 4
    - Range:
    - Constraints:

    OUTPUTS:
    - Type: a middle of the list
    - Format:Number

    EDGE CASES:
    1.
    2.
    3.

    notes:
    If the number of nodes is even, then return the second middle node.
"""

# CLARIFICATION QUESTIONS
"""
-
"""

# APPROACH
"""
0. Class definition
1. Get the input
2. Build the linked list
2. Use Two-pointer technique from start and end to find the middle
3. Verify if the nodes is even, in that case return the second middle node

TIME: O(n)
SPACE: O(1)
"""

class Node:
    def __init__ (self, val, next=None):
        self.val = val
        self.next = next

def build_list(nodes, f):
    val = next(nodes, None) #take the next value from nodes
    if val is None: #if val is None we have our list
        return None
    nxt = build_list(nodes, f) #call recursively build list
    return Node(f(val), nxt) #return a node

#Two pointer algorithm
def middle_of_linked_list(head: Node) -> int:
    left = right = head #together the pointer start from head
    while right and right.next: #until right and right.next have value
        right = right.next.next
        left = left.next
    return left.val


if __name__ == "__main__":
    head = build_list(iter(input().split()), int)
    res = middle_of_linked_list(head)
    print(res)
