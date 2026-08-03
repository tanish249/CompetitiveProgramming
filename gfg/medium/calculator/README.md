# calculator

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-03T09:30:43.548Z  

```py
class Solution:
    def utility(self, a, b, opr):
        if opr==1:
            c=a+b
            print(str(c))
        elif opr==2:
            c=a-b
            print(str(c))
        elif opr==3:
            c=a*b
            print(str(c))
        else:
            print("Invalid Input")
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/calculator/1)