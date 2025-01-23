import unittest
from typing import List

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

#Reasoning


def isPalindrome(s: str) -> bool:
    s = ''.join(char.lower() for char in s if char.isalnum())
    l = 0
    r = len(s) - 1

    while l<r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

class UnitTest(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(isPalindrome("A man, a plan, a canal: Panama"), True) # palindrome

    def test_case_1(self):
        self.assertEqual(isPalindrome("race a car"), False) # Not palindrome

    def test_case_2(self):
        self.assertEqual(isPalindrome("raceacar"), False) # Not palindrome

    def test_case_3(self):
        self.assertEqual(isPalindrome(""), True)  # Empty string

    def test_case_4(self):
        self.assertEqual(isPalindrome("12321"), True)  # Numbers

    def test_case_5(self):
        self.assertEqual(isPalindrome("0P"), False)  # Not palindrome

if __name__ == "__main__":
    unittest.main()