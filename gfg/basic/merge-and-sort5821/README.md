# Merge and Sort

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given two arrays  **arr1[]** and  **arr2[]**, return the merged array in ascending order containing unique elements.

 **Examples:** 

```
Input: arr1[] = [11, 1, 8], arr2[] = [10, 11]
Output: [1, 8, 10, 11]
Explanation: The ouput array after merging both the arrays and removing duplicates is [1, 8, 10, 11]

```

```
Input: arr1[] = [7, 1, 5, 3, 9], arr2[]  = [8, 4, 3, 5, 2, 6]
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9] 
```

 **Constraints:** 
1 ≤ arr1.size(), arr2.size() ≤ 104
0 ≤ arr1[i], arr2[i] ≤ 109

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-17T10:00:49.086Z  

```py
class Solution:
    def mergeNsort(self, arr1, arr2):
        nums =list(set(arr1 + arr2))

        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2

        left = self.mergeNsort(nums[:mid], [])
        right = self.mergeNsort(nums[mid:], [])

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
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/merge-and-sort5821/1)