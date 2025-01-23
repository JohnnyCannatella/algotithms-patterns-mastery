#!/bin/python3
import os
import unittest
from typing import List

"""
Problem: https://leetcode.com/problems/two-sum-iii-data-structure-design/
DATE: 20/01/25
TOPIC: data structure, python basic

INPUT:
- array of string (rappresent the command)
- array of number (rappresente the nums to add o find)
OUTPUT:
- void if add number
- true or false if there exist any pair of numbers 
EDGE CASES:
- none value
- more array of command then array of number
NOTE:
- if twosum I have to init the twoSum array
SPACE:
TIME:
 
PSEUDOCODE

"""

class TwoSum:

    def __init__(self):
        self.num_counts = {} #init empty dict

    def add(self, number: int) -> None:
        self.num_counts[number] = self.num_counts.get(number, 0) + 1 #count the number on the dict

    def find(self, value: int) -> bool:
        for num in self.num_counts:
            complement = value - num
            if complement in self.num_counts:
                # Se cerchiamo lo stesso numero, ne servono almeno 2
                if complement == num:
                    if self.num_counts[num] > 1:
                        return True
                else:
                    return True
        return False

class UnitTest(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual()

    def test_example_case_2(self):
        self.assertEqual()

if __name__ == "__main__":
    UnitTest()