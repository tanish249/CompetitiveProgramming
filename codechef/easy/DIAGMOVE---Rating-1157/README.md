# DIAGMOVE - Rating 1157

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Diagonal movement

Given the coordinates $(x, y)$ of a point in 2-D plane. Find if it is possible to reach $(x, y)$ from $(0, 0)$. The only possible moves from any coordinate $(i, j)$ are as follows:

- Go to the point with coordinates $(i + 1, j + 1)$.
- Go to the point with coordinates $(i + 1, j - 1)$
- Go to the point with coordinates $(i - 1, j + 1)$.
- Go to the point with coordinates $(i - 1, j - 1)$.
### Input Format
- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of a single line of input, two integers $x, y$.
### Output Format

For each test case, print `YES` if it is possible to reach $(x, y)$ from $(0, 0)$, otherwise print `NO`.

You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

### Constraints
- $1 \leq T \leq 2\cdot10^4$
- $-10^9 \leq x, y \leq 10^9$
### Sample 1:
Input
Output

```
6
0 2
1 2
-1 -3
-1 0
-3 1
2 -1

```

```
YES
NO
YES
NO
YES
NO

```

### Explanation:

 **Test case $1$** : A valid sequence of moves can be: $\;(0, 0) \rightarrow (1, 1) \rightarrow (0, 2)$.

 **Test case $2$** : There is no possible way to reach the point $(1, 2)$ from $(0, 0)$.

 **Test case $3$** : A valid sequence of moves can be: $\;(0, 0) \rightarrow (-1, -1) \rightarrow (0, -2) \rightarrow (-1, -3)$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-18T06:50:28.246Z  

```py
t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=abs(a)
    g=abs(b)
    p=h+g
    if p%2==0:
        print("YES")
    else:
        print("NO")
```

---

[View on CodeChef](https://www.codechef.com/problems/DIAGMOVE)