# MISSINGNUM7 - Rating 151

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Missing Number

Chef had $4$ pieces of paper with him, one paper with $1$ written on it, one paper with $2$, one paper with $3$ and finally one paper with $4$.

Now, Chef lost one of the pieces of paper, and noticed that the other numbers on his papers add up to $S$. Find the number on the missing paper.

### Input Format
- The first and only line of input contains a single integer $S$.
### Output Format

Output the number on the missing paper.

### Constraints
- $6 \le S \le 9$
### Sample 1:
Input
Output

```
6

```

```
4

```

### Explanation:

Chef has the papers $1$, $2$ and $3$ with him; as they add up to $6$, so the missing has to be $4$.

### Sample 2:
Input
Output

```
9

```

```
1

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-04T04:36:01.475Z  

```py
a=int(input())
f=1+2+3
g=2+3+4
h=1+3+4
if a==f:
    print(4)
elif a==g:
    print(1)
elif a==h:
    print(2)
else:
    print(3)
```

---

[View on CodeChef](https://www.codechef.com/problems/MISSINGNUM7)