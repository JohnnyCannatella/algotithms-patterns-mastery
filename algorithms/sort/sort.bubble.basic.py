from typing import List

"""
    Excercise:
        Sort an unsorted list with bubble sort algorithm
    Arg:
        data: a list of unsorted numbers
    Return:
        a sorted list
"""


# ITSI -> O(n^2)
# Iterate through all list elements in reversed order
# Track whether a swap occurred in this pass
# Swap if the element found is greater than the next element
# If no two elements were swapped, the list is sorted

def sort_list(unsorted_list: List[int]) -> List[int]:
    n = len(unsorted_list)

    # Iterate through all list elements in reversed order
    for i in reversed(range(n)):

        # Track whether a swap occurred in this pass
        swapped = False
        for j in range(i):

            # Swap if the element found is greater than the next element
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
                swapped = True

        # If no two elements were swapped, the list is sorted
        if not swapped:
            return unsorted_list
    return unsorted_list


if __name__ == "__main__":
    unsorted_list = [int(x) for x in input().split(',')]
    res = sort_list(unsorted_list)
    print(' '.join(map(str, res)))
