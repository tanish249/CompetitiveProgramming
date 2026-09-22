# Palindrome String

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given a string  **s**, find if it is a palindrome. A string is considered a palindrome if it reads the same forwards and backwards.

 **Examples :** 

```
Input: s = "abba"
Output: true
Explanation: "abba" reads the same forwards and backwards, so it is a palindrome.
```

```
Input: s = "abc" 
Output: false
Explanation: "abc" does not read the same forwards and backwards, so it is not a palindrome.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-22T17:36:58.889Z  

```py
class Solution:
    def isPalindrome(self, s):
        h=s[::-1]
        if h==s:
            return True
        else:
            return False
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/palindrome-string0817/1)