# RECSQ - Rating 144

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Rectangle and Square

You have a rectangle of length $A$ units and breadth $B$ units. You also have a square with side length of $C$ units.

Check if both the rectangle and the square have the same area. Print $\text{Yes}$ if they have the same area, and $\text{No}$ otherwise.

### Input Format
- The first and only line of input contains $3$ integers - $A$, $B$ and $C$.
### Output Format

Output on a new line $\text{Yes}$ if they have the same area, and $\text{No}$ otherwise.

It is allowed to print each character in either case, i.e. $\text{YES}$, $\text{yes}$, $\text{yES}$ will all be accepted as a positive response.

### Constraints
- $1 \le A, B, C \le 10$
### Sample 1:
Input
Output

```
2 8 4

```

```
Yes
```

### Explanation:

Both the rectangle and the square have an area of $16$ units$^2$.

### Sample 2:
Input
Output

```
3 5 4

```

```
No
```

### Explanation:

The rectangle has an area of $15$ units$^2$ but the square has $16$ units$^2$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-24T09:03:54.432Z  

```py
a,b,c=map(int,input().split())
h=a*b
g=c*c
if h==g:
    print("YES")
else:
    print("NO")
```

---

[View on CodeChef](https://www.codechef.com/problems/RECSQ)