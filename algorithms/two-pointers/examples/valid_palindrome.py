#EXAMPLE - TWO POINTERS -> Opposite direction
#!/bin/python3
import unittest
from typing import List

# EXCERCISE
"""
    Problem:
    Determine whether a string is a palindrome, ignoring non-alphanumeric characters and case.
    
    INPUTS:
    - Type: String
    - Range: [2, 3, 4, 5, 8, 11, 18] -> target sum 8
    - Constraints: 
    
    OUTPUTS:
    - Type: Boolean
    - Format: -
    
    EDGE CASES:
    1. empty string -> error
    2. Do 1 geese see God? -> true
    
    NOTE:
    - Palindrome -> is a word, phrase or num that is reads the same way, right -> left and left-> right
        - example: Do geese see God?
"""

# CLARIFICATION QUESTIONS
"""
"""

# APPROACH
"""
- I have to remove non-alphanumeric characters and case
- I have to use two pointers pattern in opposite mode to confront the words
- init l,r -> 0,len(text)
- while l=r
            
TIME: O(n)
SPACE: O(n) 
"""

def is_palindrome(s: str) -> bool:
    s = ''.join(char.lower() for char in s if char.isalnum()) #O(N) # remove non-alphanumeric characters
    l, r = 0, len(s) -1 #O(1)
    while l<r: #O(N)
        if(s[l] != s[r]): #O(1)
            return False # Not a palindrome
        l += 1 #O(1)
        r -= 1 #O(1)
    return True # Is a palindrome

class UnitTest(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(is_palindrome("Do geese see God?"), True)

    def test_empty_string(self):
        self.assertEqual(is_palindrome(""), True)

    def test_example_case_false(self):
        self.assertEqual(is_palindrome("This test isn't good"), False)

if __name__ == "__main__":
    UnitTest()



