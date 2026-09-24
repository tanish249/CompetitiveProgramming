# Convert String to Lower Case

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given a string  **s**. The task is to convert string characters to  **lowercase**.

 **Examples:** 

```
Input: s = "ABCddE"
Output: "abcdde"
Explanation: A, B, C and E are converted to a, b, c and e thus all uppercase characters of the string converted to lowercase letter.
```

```
Input: s = "LMNOppQQ"
Output: "lmnoppqq"
Explanation: L, M, N, O, and Q are converted to l, m, n, o and q thus all uppercase characters of the string converted to lowercase letter.
```

 **Constraints:** 
1 ≤ s.size() ≤ 106

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-24T15:51:19.752Z  

```py
class Solution:
    def toLower (self, s: str) -> str:
        return s.lower()
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/convert-string-to-lowercase/1)