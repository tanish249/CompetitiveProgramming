# Palindrome Digit Sum

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given a number  **n**. Return  **true** if the digit sum(or sum of digits) of n is a Palindrome number otherwise  **false**.
A Palindrome number is a number that stays the same when reversed

 **Examples:** 

```
Input: n = 56
Output: true
Explanation: The digit sum of 56 is 5+6 = 11. Since, 11 is a palindrome number.Thus, answer is true.
```

```
Input: n = 98
Output: false
Explanation: The digit sum of 98 is 9+8 = 17. Since 17 is not a palindrome,thus, answer is false.
```

 **Constraints:** 
1 ≤ n ≤ 109

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-13T09:47:34.369Z  

```py
class Solution:
    def isDigitSumPalindrome(self, n):
        h=list(map(int,str(n)))
        g=sum(h)
        f=str(g)
        d=int(f[::-1])
        if d==g or g==d:
            return True
        else:
            return False
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/sum-of-digit-is-pallindrome-or-not2751/1)