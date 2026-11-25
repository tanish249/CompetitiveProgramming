# DECINC - Rating 718

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-25T12:13:42.034Z  

```py
t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    h=a/b
    g=c/d
    if h==g:
        print("Equal")
    elif h>g:
        print("Alice")
    else:
        print("Bob")
```

---

[View on CodeChef](https://www.codechef.com/problems/DECINC)