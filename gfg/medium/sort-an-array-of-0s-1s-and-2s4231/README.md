# Sort 0s, 1s and 2s

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array  **arr[]**  containing only **0s, 1s, and 2s.**  Sort the array in ascending order. 
 **Note:**  You need to solve this problem without utilizing the built-in sort function.

 **Examples:** 

```
Input: arr[] = [0, 1, 2, 0, 1, 2]
Output: [0, 0, 1, 1, 2, 2]
Explanation: 0s, 1s and 2s are segregated into ascending order.
```

```
Input: arr[] = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
Explanation: 0s, 1s and 2s are segregated into ascending order.
```

 **Follow up:**  Could you come up with a one-pass algorithm using only constant extra space?

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-22T18:19:54.130Z  

```py
class Solution:
    def sort012(self, arr):

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            result = []
            i = 0
            j = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            while i < len(left):
                result.append(left[i])
                i += 1

            while j < len(right):
                result.append(right[j])
                j += 1

            return result

        arr[:] = merge_sort(arr)
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1)