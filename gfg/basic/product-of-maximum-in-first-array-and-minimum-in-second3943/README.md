# Max and Min Product from 2 Arrays

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given two arrays of arr1 and arr2, the task is to calculate the product of the maximum element of the first array arr1, and minimum element of the second array arr2.

 **Examples :** 

```
Input : arr1[] = [5, 7, 9, 3, 6, 2],  arr2[] = [1, 2, 6, 1, 9]
Output : 9
Explanation: The max in arr1 is 9. The min element in arr2 is 1. The product is 9*1 = 9.

```

```
Input : arr1[] = [0, 0, 0, 0],  arr2[] = [1, 1, 2]
Output : 0

```

 **Constraints:** 
1 ≤ arr1.size(), arr2.size() ≤ 106
0 ≤ arr1[i], arr2[i] ≤ 108

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-15T10:15:54.610Z  

```py


class Solution:
    
    def minMaxProduct(self, arr1, arr2):
        h=max(arr1)
        g=min(arr2)
        return h*g

```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/product-of-maximum-in-first-array-and-minimum-in-second3943/1)