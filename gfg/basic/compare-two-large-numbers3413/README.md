# Compare two Large Numbers

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given two non-negative integers  **a**  and  **b**  represented as strings, compare them.

- Return 1 if a < b 
- Return 2 if a > b
- Return 3 if a = b.

 **Note:** The strings may contain leading zeros.

 **Examples:** 

```
Input: a = "1234", b = "12345"
Output: 1
Explanation: 1234 is less than 12345, so return 1.
```

```
Input: a = "100", b = "000000100"
Output: 3
Explanation: After ignoring leading zeros, both represent 100, so return 3.
```

**Constraints:
**1<=a.size(), b.size()<=155
Both string a and b contains character '0' to '9'

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-19T13:56:28.320Z  

```py
class Solution:
    def check(self, a, b):
        a=int(a)
        b=int(b)
        if a<b:
            return 1
        elif a>b:
            return 2
        elif a==b:
            return 3
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/compare-two-large-numbers3413/1)