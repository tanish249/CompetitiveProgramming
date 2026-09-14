# Binary Search

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given an array  **arr[],** sorted in ascending order and an integer  **k**. Return true if k is present in the array, otherwise, false.

 **Examples:** 

```
Input: arr[] = [1, 2, 3, 4, 6], k = 6
Output: true
Exlpanation: Since, 6 is present in the array at index 4 (0-based indexing), output is true.
```

```
Input: arr[] = [1, 2, 4, 5, 6], k = 3
Output: false
Exlpanation: Since, 3 is not present in the array, output is false.
```

```
Input: arr[] = [2, 3, 5, 6], k = 1
Output: false1 ≤ arr[i] ≤ 106
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-14T15:57:25.301Z  

```py
class Solution:
    def binarySearch(self, arr, k):
        left = 0
        right = len(arr) - 1
        while left <=right:
            mid = (left + right ) // 2
            if k ==arr[mid]:
                return True
            elif k > arr[mid]:
                left = mid + 1
            elif k < arr[mid]:
                right = mid - 1
        else:
            return False
            
            
    
         
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/who-will-win-1587115621/1)