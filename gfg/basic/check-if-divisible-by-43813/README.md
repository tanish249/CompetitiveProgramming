# Check if divisible by 4

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given a number in form of a string  **s**. Check whether it is  **divisible by 4**  or not.

 **Examples :** 

```
Input: s = "1124"
Output: true
Explanation: The last two digits of "1124" are 24. Since 24 is divisible by 4, the given number is also divisible by 4. Hence, the output is true.

```

```
Input: s = "7"
Output: false
Explanation: As 7 % 4 = 3, the number is not divisible by 4. Hence, the output is false.

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-19T13:33:43.101Z  

```py
class Solution:
    def divisibleBy4(self, s):
        h = int(s)

        if h % 4 == 0:
            return True
        else:
            return False
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/check-if-divisible-by-43813/1)