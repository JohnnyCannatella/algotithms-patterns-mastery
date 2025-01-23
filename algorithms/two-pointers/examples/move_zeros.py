#EXAMPLE - TWO POINTERS -> Same Direction
#!/bin/python3
from typing import List
import unittest

# EXCERCISE
"""
    Problem:
    Given an array of integers, move all the 0s to the back of the array while maintaining the relative order of the non-zero elements. 
    Do this in-place using constant auxiliary space.
    
    INPUTS:
    - Type: Array
    - Range: [1, 0, 2, 0, 0, 7]
    - Constraints: 
    
    OUTPUTS:
    - Type: Array of int
    - Format: -
    
    EDGE CASES:
    1. [] -> Result []
    2. [1,2,7] -> No change 
    3. [0,0,0] -> [0,0,0]
    
    NOTE:
    - In-place -> We have to use the same array
    - constant auxiliary space -> 
"""

# CLARIFICATION QUESTIONS
"""
    Q: Should we consider case sensitivity?
    A: No, ignore case
    
    Q: How should we handle non-alphanumeric characters?
    A: Ignore them
    
    Q: What about empty strings?
    A: Consider them palindromes

"""

# APPROACH
"""

TIME: O(n)
SPACE: O(1) modify in place
"""

def move_zeros(nums: List[int])-> List[int]:
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
    return nums


class TestMoveZeros(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(move_zeros([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])

    def test_empty_array(self):
        self.assertEqual(move_zeros([]), [])

    def test_no_zeros(self):
        self.assertEqual(move_zeros([1, 2, 3]), [1, 2, 3])

    def test_all_zeros(self):
        self.assertEqual(move_zeros([0, 0, 0]), [0, 0, 0])

    def test_mixed_numbers(self):
        self.assertEqual(move_zeros([0, -1, 0, 2, -3]), [-1, 2, -3, 0, 0])

if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    move_zeros(nums)
    print("".join(map(str, nums)))
    unittest.main()