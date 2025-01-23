#!/bin/python3

"""
    excercises:
        Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
        Then print the respective minimum and maximum values as a single line of two space-separated long integers.
    arg:
        array of positive integers -> Example [5,6,3,1,8]
    output:
         print the respective minimum and maximum value
    steps:
        - Get the array of integer num
        - Set all the combination
        - Find minimum and maximum value of the array
    question:
        - can a use a built-in function as sum, min, max
"""


def miniMaxSum(arr):
    total_sum = sum(arr)
    min_val = min(arr)
    max_val = max(arr)

    min_sum = total_sum - max_val
    max_sum = total_sum - min_val

    print(f"{min_sum} {max_sum}")


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
