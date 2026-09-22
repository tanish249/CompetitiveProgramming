# Kth Smallest

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array  **arr[]**  and an integer  **k**, find and return the kth smallest element in the given array.

 **Examples :** 

```
Input: arr[] = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10], k = 4
Output: 5
Explanation: 4th smallest element in the given array is 5.
```

```
Input: arr[] = [7, 10, 4, 3, 20, 15], k = 3
Output: 7
Explanation: 3rd smallest element in the given array is 7.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-22T17:50:40.210Z  

```py
class Solution:
    def kthSmallest(self, arr, k):

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

        arr = merge_sort(arr)
        return arr[k - 1]
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/kth-smallest-element5635/1)