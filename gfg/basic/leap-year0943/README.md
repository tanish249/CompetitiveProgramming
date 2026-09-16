# Leap Year

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

You are given an Integer  **n**. Return  **true** if It is a Leap Year otherwise return  **false**.

 **Examples:** 

```
Input: n = 4
Output: true
Explanation: 4 is not divisible by 100 and is divisible by 4 so its a leap year
```

```
Input: n = 2021
Output: false
Explanation: 2021 is not divisible by 100 and is also not divisible by 4 so its not a leap year
```

 **Constraints:** 
1<= n < 104

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-16T16:43:31.641Z  

```py
class Solution:
    def checkYear (self, n):
        if n%400==0 and n%100==0:
            return True
        elif n%4==0 and n%100!=0:
            return True
        else:
            return False
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/leap-year0943/1)