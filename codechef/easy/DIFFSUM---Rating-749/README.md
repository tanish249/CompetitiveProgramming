# DIFFSUM - Rating 749

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Sum OR Difference

Write a program to take two numbers as input and print their difference if the first number is greater than the second number $otherwise$ print their sum.

### Input Format

First line will contain two numbers, $(N1)$ and $(N2),$ separated by a space.

### Output Format

Output a single line containing the difference of 2 numbers $(N1 - N2)$ if the first number is greater than the second number otherwise output their sum $(N1 + N2)$.

### Constraints
- $-1000 \leq N1 \leq 1000$
- $-1000 \leq N2 \leq 1000$
### Sample 1:
Input
Output

```
82 28
```

```
54
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-01T08:09:50.715Z  

```py
a=int(input())
b=int(input())
if a>b:
    print(a-b)
else:
    print(a+b)
```

---

[View on CodeChef](https://www.codechef.com/problems/DIFFSUM)