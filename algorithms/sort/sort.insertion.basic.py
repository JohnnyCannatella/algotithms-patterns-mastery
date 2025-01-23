from typing import List

# FCS -> O(n^2)
# F -> First Element is considered sorted
# C -> Compare the current element with current element less 1 and gets the smallest
# S -> swaps current smaller element with the element before it

# Stable sortable algorithm: [1, 3, 2, 7, 7, 6, 9, 10, 9] -> [1, 2, 3, 6, 7, 7, 9, 9, 10]
#TIME COMPLEXITY -> O(N^2)
def insertion_sort(unsorted_list: list[int]) -> List[int]:
    # F -> First Element is considered sorted
    for i in enumerate(unsorted_list):  #O(N)
        current = i  #O(1)
        # gets the smallest element and inserts it at current index
        while current > 0 and unsorted_list[current] < unsorted_list[current - 1]:  #O(1) to #O(N^2)
            # swaps current smaller element with the element before it
            unsorted_list[current], unsorted_list[current - 1] = unsorted_list[current - 1], unsorted_list[
                current]  #O(1)
            current -= 1  #O(1)

    return unsorted_list


if __name__ == '__main__':
    unsorted_list = [int(x) for x in input("Enter your num here:").split(',')]
    sortedList = insertion_sort(unsorted_list)
    print(''.join(map(str, sortedList)))

