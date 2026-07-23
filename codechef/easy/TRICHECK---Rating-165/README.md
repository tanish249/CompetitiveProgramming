# TRICHECK - Rating 165

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Triangle Checking

You are given $3$ sticks of length $A$, $B$ and $C$.

Please check if they can be the side lengths of a valid non-degenerate triangle.

Recall that $A, B$ and $C$ can be the side-lengths of a non-degenerate triangle if and only if each of the following $3$ conditions hold:

- $A + B > C$
- $B + C > A$
- $A + C > B$
### Input Format
- The first and only line of input contains $3$ integers - $A, B$ and $C$.
### Output Format

For each test case, output on a new line $\text{Yes}$ if the side lengths form a valid triangle, and else $\text{No}$.

It is allowed to print each character in either case. For example, $\text{YES}$, $\text{yes}$ and $\text{yEs}$ will all be accepted as positive responses.

### Constraints
- $1 \le A, B, C \le 10$
### Sample 1:
Input
Output

```
2 3 4

```

```
Yes
```

### Explanation:

All the conditions are satisfied and so it is a valid triangle.

### Sample 2:
Input
Output

```
4 6 2

```

```
No

```

### Explanation:

The condition $A + C > B$ is not true here, hence it is not valid.

### Sample 3:
Input
Output

```
9 9 9

```

```
Yes
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-23T16:19:14.109Z  

```py
a,b,c=map(int,input().split())
if(a+b>c and a+c>b and b+c>a):
    print("YES")
else:
    print("N")
```

---

[View on CodeChef](https://www.codechef.com/problems/TRICHECK)