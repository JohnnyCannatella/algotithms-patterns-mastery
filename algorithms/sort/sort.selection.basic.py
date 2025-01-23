from typing import List

"""
    Excercise:
        Sort an unsorted list with selection sort algorithm
    Arg:
        data: a list of unsorted numbers
    Return:
        a sorted list
"""

# AFSR -> O(n^2)
# Assume the current position is minimum
# Find the minimum index from the rest of the list
# swap the minimum element with the i element of the unsorted part
# repeat until the entire array is sorted

def selection_sort(unsorted_list: list[int]) -> List[int]:
    n = len(unsorted_list)
    for i in range(n):
        min_index = i

        for j in range(i, n):
            if unsorted_list[j] < unsorted_list[min_index]:
                min_index = j

        unsorted_list[min_index], unsorted_list[i] = unsorted_list[i], unsorted_list[min_index]
    return unsorted_list


if __name__ == "__main__":
    unsorted_list = [int(x) for x in input().split(',')]
    res = selection_sort(unsorted_list)
    print(''.join(map(str, res)))
