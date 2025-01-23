#EXAMPLE - TWO POINTERS -> Same Direction
# Intuition
# If we could use extra memory, we could easily solve this by going through the list once and using a hash set to record elements we have seen. But we are not allowed extra memory so we have to look at the conditions and see if there's anything we could use. An important condition is that the numbers are sorted, which means the same numbers are next to each other. This means as we go through the list, once we see a number A, we will see all occurrences of A together, and will not see A again after we see B. Using this key observation, we can devise a fast/slow pointer solution.

# Time Complexity: O(n)

# We simply traverse the array once, moving from left to right.

# Space Complexity: O(1)

from typing import List

def remove_duplicates(arr: List[int]) -> int:
    left = 0
    for right in range(len(arr)):
        if arr[right] != arr[left]:
            left += 1
            arr[left] = arr[right]

    return left

if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    res = remove_duplicates(arr)
    print(" ".join(map(str, arr[:res])))