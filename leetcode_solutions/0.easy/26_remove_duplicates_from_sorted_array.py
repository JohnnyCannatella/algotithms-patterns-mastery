#!/bin/python3
import os
import unittest
from typing import List

# LEETCODE
#TOPIC: Array, Two Pointers
"""
PROBLEM: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
DATE: 4/01/25

INPUTS:
- Type: Array of num
- Constraints:
    remove the duplicates in-place
    Maintain the order the same
    1 <= nums.length <= 3 * 104
    -100 <= nums[i] <= 100
    nums is sorted in non-decreasing order.
    
OUTPUTS:
- Type: Return k -> Int
- Format:
    
EDGE CASES:
1. Example 1: [1,1,2] -> 2, nums = [1,2,_]
2. Example 2: [0,0,1,1,1,2,2,3,3,4] -> 5, nums = [0,1,2,3,4,_,_,_,_,_]
3. Example 3: [] -> 0, nums=[]
4. Example 4: [0,1,2,3,4] -> 5, nums = [0,1,2,3,4]
5. Example 5: [1,1,1] -> 1, nums = [1]
    
NOTES:

"""

# CLARIFICATION QUESTIONS
"""
I -> INTERVIEWER
M -> Me

    M: Should we consider error case ? 
    I: Generally, you don’t need to explicitly handle error cases like None or invalid input types unless specified in the problem description. 
    You can assume that nums will always be a list of integers and will be sorted in non-decreasing order.
    
    M: What I should I do with the remaining nums after the first K elements ?
    I: Once you’ve identified the first k unique elements, you don’t need to worry about the remaining elements in nums. 
    According to the problem statement, the values after index k are irrelevant, so you can leave them as they are or replace them with any value. 
    The key is to make sure the first k elements contain the unique values in the original order.
    
    M: So I have to return just the K or even the array ?
    I: You should return only the integer k, which represents the count of unique elements found in the array. 
    However, your solution should modify the input array nums in-place so that the first k elements contain the unique values in non-decreasing order. 
    The elements beyond k are not significant.
    
    M: In the edge case if array contain just duplicate I have to return K=1 ?
    I: Yes, exactly. If the array contains only duplicates, there will be only one unique value. 
    For instance, if the array is [2, 2, 2, 2], you should return k = 1, with nums[0] being 2.
    
    I:Why do you need to update nums[left] if nums[left] != nums[right]?
    M: 
    
    I: What will be the initial values of left and k, and why?
    M: 
    
    I: How do you handle the edge case when the array is empty?
    M:
    
    I: What will happen if the array contains only one element?
    M: 
    

"""

# APPROACH
"""
1. I can apply same direction two pointer technique
2. Init the pointer fast = 0 and slow = 0
3. Execute a cycle -> for fast in range(nums)
4. foreach value compare nums[fast] != nums[right]
5. if true -> switch left with right value and increment +1 of the left and k+=1 
6. return k 

TIME: 
SPACE: 
"""

def removeDuplicates(nums: List[int]) -> int:
    s = 0
    for f in range(len(nums)):
        if nums[f] != nums[s]:
            s += 1
            nums[s] = nums[f]
    return s + 1

class UnitTest(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(removeDuplicates([1,1,2]), 2)

    def test_example_case_2(self):
        self.assertEqual(removeDuplicates([0,0,1,1,1,2,2,3,3,4]), 5)

if __name__ == "__main__":
    UnitTest()