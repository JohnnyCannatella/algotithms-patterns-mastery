# Pattern Name

## 1. Conceptual Overview
- Pattern description
  - Its primary goal is to allow for constant-time range sum queries on an array
  - Running sum array where each element is sum of all previous elements
  - Categorized in: Prefix sum / Suffix sum
- When to use: 
  - Use when needing quick range sum queries or detecting cumulative patterns
- Complexity characteristics
  - Time: O(n) preprocessing, O(1) range queries 
  - Space: O(n)
- Differences from other patterns: case(Prefix Sum vs. Sliding Window):
  - While both techniques solve subarray-related problems, they have different use cases:
    - Prefix Sum: Ideal for quick range sum queries on static arrays. 
    - Sliding Window: Better for problems involving contiguous subarrays with specific conditions or sizes, e.g., maximum sum of subarrays of size 'k'.

## 2. Variations
* Forward prefix: sum[i] = sum[i-1] + nums[i]
* Backward suffix: sum[i] = sum[i+1] + nums[i]
* 2D prefix: matrix cell contains sum of rectangle from (0,0) to (i,j)
* Multiple prefix arrays for different properties (min/max/product)

## 3. Common Problem Types
- Range Sum Queries
```python
nums = [1,2,3,4,5]
prefix = [1,3,6,10,15]
# Sum of range [2,4]: prefix[4] - prefix[1] = 12
# We can use -> return list(accumulate(nums, initial=0)) instead to write down the algorithm
```

- Equilibrium Point
```python
# Find index where sum of left equals sum of right
def find_equilibrium(nums):
    total = sum(nums)
    left_sum = 0
    for i in range(len(nums)):
        if left_sum == total - left_sum - nums[i]:
            return i
        left_sum += nums[i]
```

- Subarray Sum Equals K
```python
# Count sub_arrays with sum = k using prefix sums
def subarray_sum(nums, k):
    count = prefix_sum = 0
    seen = {0:1}
    for num in nums:
        prefix_sum += num
        count += seen.get(prefix_sum - k, 0)
        seen[prefix_sum] = seen.get(prefix_sum, 0) + 1
    return count
```

- Common subarray problems
```
   1. Subarray with Given Sum: Find a contiguous subarray that sums to a target value. 
   2. Zero Sum Subarrays: Locate subarrays that sum to zero. 
   3. Longest Subarray with Sum k: Find the longest subarray with a specific sum. 
   4. Smallest Subarray with Sum > X: Identify the smallest subarray whose sum exceeds a given value. 
   5. Maximum Sum of Subarrays of Size k: Find the maximum sum among all subarrays of a fixed size. 
   6. Suffix Sum: Similar to prefix sum, but calculated from the end of the array.
```

## 4. Implementation Templates
```python
def prefix_sum_1d(nums):
    prefix = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        prefix[i+1] = prefix[i] + nums[i]
    return prefix

def prefix_sum_2d(matrix):
    if not matrix: return []
    m, n = len(matrix), len(matrix[0])
    prefix = [[0]*(n+1) for _ in range(m+1)]
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            prefix[i][j] = (prefix[i-1][j] + prefix[i][j-1] - 
                           prefix[i-1][j-1] + matrix[i-1][j-1])
    return prefix
```
## 4. Implementation Approach
### two-pass approach
```
1. Initialize the result array with 1s.
2. Compute the prefix product:
    • Traverse the array from left to right.
    • For each element, multiply it by the running product and store in the result array.
3. Compute the suffix product:
    • Traverse the array from right to left.
    • Maintain a running product from the right.

For each element, multiply the current result by the running product.
This two-pass approach ensures that for each index, we have the product of all elements to its left and all elements to its right, without including the element itself.
```

## 6. keywords
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