# Sum Of Digits

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a positive number  **n**. Find the  **sum**  of all the digits of n.

 **Examples:** 

```
Input: n = 687
Output: 21
Explanation: Sum of 687's digits: 6 + 8 + 7 = 21
```

```
Input: n = 12
Output 3
Explanation: Sum of 12's digits: 1 + 2 = 3

```

 **Constraints:** 
1 <= n <= 105

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-13T09:30:08.754Z  

```py
class Solution:
    def sumOfDigits(self, n):
       h=list(map(int,str(n)))
       return sum(h)
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/sum-of-digits1742/1)