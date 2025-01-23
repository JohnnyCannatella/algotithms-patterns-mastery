# EXAMPLE - TWO POINTERS -> Opposite direction
# !/bin/python3
import unittest
from typing import List

# EXCERCISE
"""
    Problem:
    Given an array representing heights of vertical lines, find the maximum area of water trapped between two lines.

    INPUTS:
    - Type: array of int
    - Range: [1,8,6,2,5,4,8,3,7]
    - Constraints: 

    OUTPUTS:
    - Type: Int
    - Format: -

    EDGE CASES:
    1.Example: Input: [1,8,6,2,5,4,8,3,7] - Output: 49.
    2.empty array -> error
    3.

    NOTE:
    - 
"""

# CLARIFICATION QUESTIONS
"""
    Q: Can it contains negative numbers ?
    A: No, ignore case

    Q: Can consider the array sorted ?
    A: yes
"""

# APPROACH
"""
- 

NOTE

TIME:
SPACE: O(n) return new var
"""


def container_with_most_water(height: List[int]) -> int:
    left, right = 0, len(height) -1
    max_area = 0
    while left < right:
        current_area = (right - left)* (min(height[left],height[right]))
        max_area = max(max_area, current_area)
        if height[left] < height[right]:
            left+=1
        else:
            right-=1
    return max_area


class UnitTest(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)

    def test_empty_array(self):
        self.assertEqual(container_with_most_water([]), 0)

    def test_example_case_2(self):
        self.assertEqual(container_with_most_water([1, 1]), 1)


if __name__ == "__main__":
    arr = (int (x) for x in input.split())
    res = container_with_most_water(arr)
    print(res)
    UnitTest()



