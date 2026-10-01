# FLOW007 - Rating 588

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Reverse The Number

Given an Integer  **N**, write a program to reverse it.

### Input

The first line contains an integer  **T**, total number of testcases. Then follow  **T**  lines, each line contains an integer  **N**.

### Output

For each test case, display the reverse of the given number  **N**, in a new line.

### Constraints
- 1 ≤ T ≤ 1000
- 1 ≤ N ≤ 1000000
### Sample 1:
Input
Output

```
4
12345
31203
2123
2300
```

```
54321
30213
3212
32
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-01T15:05:15.681Z  

```py
t=int(input())
for _ in range(t):
    a=input()
    h=str(a)[::-1]
    print(int(h))
```

---

[View on CodeChef](https://www.codechef.com/problems/FLOW007)