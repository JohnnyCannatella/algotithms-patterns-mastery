import unittest
from typing import List

"""
Problem: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
DATE: 4/01/25
TOPIC: Two Pointers, String, String Matching

INPUTS:
– Two strings

CONSTRAINTS:
1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.

OUTPUTS:
- return the index of the first occurrence of needle in haystack
- or -1 if needle is not part of haystack.

EDGE CASES:

TIME: 

SPACE: 

NOTES:
- The order of the elements may be changed

QUESTION: I -> INTERVIEWER - M -> Me

    M: Should we consider error case ? 
    I: Generally
    
"""

#Reasoning
# We can use two pattern technic ->  opposite direction
# the opposite direction pattern differs in the use of while cycle
#

def strStr(haystack: str, needle: str) -> int:
    # Se needle è più lungo di haystack, impossibile trovarlo
    if len(needle) > len(haystack):
        return -1

    left = 0  # puntatore per haystack
    while left <= len(haystack) - len(needle):
        right = 0  # puntatore per needle

        # Finché i caratteri corrispondono, avanziamo right
        while right < len(needle) and haystack[left + right] == needle[right]:
            right += 1

        # Se right ha raggiunto la fine di needle, abbiamo trovato un match
        if right == len(needle):
            return left

        left += 1  # Proviamo la prossima posizione in haystack

    return -1


class UnitTest(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(strStr("sadbutsad", "sad"), 0)

    def test_example_case_2(self):
        self.assertEqual(strStr("leetcode", "leeto"), -1)

if __name__ == "__main__":
    UnitTest()