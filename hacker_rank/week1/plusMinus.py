import math
import os
import random
import re
import sys

"""
    Excercise:
        Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
        Print the decimal value of each fraction on a new line with  places after the decimal.
        Note: This challenge introduces precision leetcode_solutions. The test cases are scaled to six decimal places, 
        though answers with absolute error of up to  are acceptable.
    Arg:
        data: an array of integers
    Output:
        Print: Ratios of positive, negative and zero values in the array with 6 places after the decimal.
    Steps:
        - Get an array of values
        - Initiliaze necessary variables
        - Foreach value of array verify is positive,negative,zero
        - Count the same type of value
        - Print results
"""

"""
    ERRORS:
        Formattazione dell'output: Il problema richiede 6 cifre decimali.
        Input: L'input dovrebbe essere gestito come specificato nel problema.
        Sorting dell'array: Non è necessario ordinare l'array per questo problema.
"""
def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    n = len(arr)

    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zero += 1
    print(f"{positive/n:.6f}")
    print(f"{negative/n:.6f}")
    print(f"{zero/n:.6f}")


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
