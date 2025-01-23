import unittest
from typing import List

"""
Problem: https://leetcode.com/problems/remove-element/
DATE: 4/01/25
TOPIC: Array, Two Pointers

INPUTS:
– nums -> Array []
- val -> Int

CONSTRAINTS:
- Use in place array
- 0 <= nums.length <= 100
- 0 <= nums[i] <= 50
- 0 <= val <= 100

OUTPUTS:
Return K -> the number of elements in nums which are not equal to val.

EDGE CASES:

TIME: 

SPACE: 

NOTES:
- The order of the elements may be changed

QUESTION: I -> INTERVIEWER - M -> Me

    M: Should we consider error case ? 
    I: Generally
    
"""

def removeElement(nums: List[int], val: int) -> int:
    s = 0
    for f in range(len(nums)):
        if nums[f] != val:
            nums[s] = nums[f]
            s+=1
    return s


class UnitTest(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(removeElement([3,2,2,3], 3), 2)

    def test_example_case_2(self):
        self.assertEqual(removeElement([0,1,2,2,3,0,4,2], 2), 5)

if __name__ == "__main__":
    UnitTest()