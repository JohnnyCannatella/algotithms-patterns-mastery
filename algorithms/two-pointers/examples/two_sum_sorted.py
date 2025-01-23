#EXAMPLE - TWO POINTERS -> Opposite direction
#!/bin/python3
from typing import List

# EXCERCISE
"""
    Problem:
   Given an array of integers sorted in ascending order, find two numbers that add up to a given target. Return the indices of the two numbers in ascending order. 
   You can assume elements in the array are unique and there is only one solution. Do this in O(n) time and with constant auxiliary space.
    
    INPUTS:
    - Type: A sorted Int array
    - Range: [2, 3, 4, 5, 8, 11, 18] -> target sum 8
    - Constraints: 
    
    OUTPUTS:
    - Type: Index of the nums that added up reach the target sum
    - Format: int
    
    EDGE CASES:
    1. [] -> Error
    2. [1,2,7] -> Target: 0 -> Error
    3. [0,0,0] -> [0,0,0]
    
    NOTE:
    - Do this in O(n) time
    - use constant auxiliary space.
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
- Get the array and the target
- Init pointer
- Cycle
- 

NOTE
- We can solve it even with brute force
n = len(arr)
for i in range(n):
    for j in range(n):
        if arr[i] + arr[j] == target:
            return i, j
            
TIME: O(n)
SPACE: O(1) modify in place
"""

def sum_sorted(arr: List[int], target: int) -> List[int]:
    l, r = 0, len(arr) - 1
    while l < r:
        two_sum = arr[l]+ arr[r]
        if two_sum == target:
            return [l, r]
        if two_sum > target:
            r -= 1
        else:
            l += 1


if __name__ == "__main__":
    nums = [int (x) for x in input().split()]
    target = int(input())
    res = sum_sorted(nums, target)
    print("".join(map(str, res)))
