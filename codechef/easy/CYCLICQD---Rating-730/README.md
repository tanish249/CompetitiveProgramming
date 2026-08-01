# CYCLICQD - Rating 730

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-01T08:56:14.664Z  

```py
t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())

    h = b * 3
    g = a - b
    j = g * -1
    p = h + j

    if p >= c:
        print("PASS")
    else:
        print("FAIL")
```

---

[View on CodeChef](https://www.codechef.com/problems/CYCLICQD)