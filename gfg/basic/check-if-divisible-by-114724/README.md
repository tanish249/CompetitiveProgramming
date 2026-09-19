# Check if divisible by 11

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given a number  **s**. Check whether it is divisble by 11 or not.

 **Examples:** 

```
Input: s = 76945
Output: true
Explanation: The number is divisible by 11 as 76945 % 11 = 0.

```

```
Input: s = 12
Output: false
Explanation: The number is not divisible by 11 as 12 % 11 = 1.

```

 **Constraints:** 
1 ≤ |s| ≤ 101000+5

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-19T13:54:31.428Z  

```py
class Solution:
    def divisibleBy11(self, s: str) -> bool:
        s=int(s)
        if s%11==0:
            return True
        else:
            return False
       
      
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/check-if-divisible-by-114724/1)