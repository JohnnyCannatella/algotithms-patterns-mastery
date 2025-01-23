# Sliding window Pattern

**Description**
Its primary goal is to allow for constant-time range sum queries on an array.
The prefix sum of an array at index 'i' is the sum of all numbers from index '0' to 'i'. By computing and storing the prefix sum of an array, you can easily answer queries about the sum of any subarray in constant time.

## Example for Prefix Sum in Python
```def prefix_sum_array(arr):
    prefix_sum = [0]
    for num in arr:
        prefix_sum.append(prefix_sum[-1] + num)
    return prefix_sum
```

**Prefix Sum vs. Sliding Window**
While both techniques solve subarray-related problems, they have different use cases:
• Prefix Sum: Ideal for quick range sum queries on static arrays.
• Sliding Window: Better for problems involving contiguous subarrays  with specific conditions or sizes, e.g., maximum sum of subarrays of size 'k'.

**Common Uses**
1. Subarray with Given Sum: Find a contiguous subarray that sums to a target value.
2. Zero Sum Subarrays: Locate subarrays that sum to zero.
3. Longest Subarray with Sum k: Find the longest subarray with a specific sum.
4. Smallest Subarray with Sum > X: Identify the smallest subarray whose sum exceeds a given value.
5. Maximum Sum of Subarrays of Size k: Find the maximum sum among all subarrays of a fixed size.
6. Suffix Sum: Similar to prefix sum, but calculated from the end of the array.

**Note**
Suffix Sum
Just as we have a prefix sum that calculates the sum from the beginning to a specific index, 
we can also calculate a suffix sum, which calculates the sum from a particular index to the end of the array.


**Classification**
1. Prefix sum
```
```

2. Suffix sum
```
```

**keywords**
```
"Range sum"
"Sum of subarray"
"Cumulative sum"
"Find sum between index i and j"
"Running sum"
"Continuous sequence sum"
"Accumulative sum"
"Sum queries"
```

**Warning Signs (quando il prefix sum potrebbe essere utile):**

"Need to calculate same sum multiple times"
"Time limit exceeded with brute force approach"
"Optimize sum calculation"
"Large number of sum queries"