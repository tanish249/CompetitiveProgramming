# LB03B - Rating 580

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-10T08:13:37.399Z  

```py
# Update the program below to solve the problem

t = int(input())            
for i in range(t):          
    a,b,c= map(int, input().split())
    if c%a==0 and c%b==0:
        print("ANY")
    elif c%a==0:
        print("CHICKEN")
    elif c%b==0:
        print("DUCK")
    else:
        print("NONE")
```

---

[View on CodeChef](https://www.codechef.com/problems/LB03B)