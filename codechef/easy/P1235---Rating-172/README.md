# P1235 - Rating 172

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Contest Registration Fee

A contest is being organized where registration is free for the first $X$ users. Every user who registers after that has to pay a fee of $100$ rupees.

Alice registered at position $Y$. Determine the amount she has to pay.

### Input Format
- The first and only line of input contains two space-separated integers $X$ and $Y$ — the number of free registrations allowed and Alice's registration position, respectively.
### Output Format

Print a single integer denoting the amount Alice has to pay.

### Constraints
- $1 \leq X,Y \leq 10$
### Sample 1:
Input
Output

```
1 1

```

```
0
```

### Explanation:

$X = 1$ and $Y = 1$. Registration is free for only the first user, and Alice registered at position $1$, which is within the free window. Hence, she pays $0$.

### Sample 2:
Input
Output

```
2 5

```

```
100
```

### Explanation:

$X = 2$ and $Y = 5$. Registration is free for the first $2$ users only, but Alice registered at position $5$, which falls outside the free window. Hence, she has to pay $100$ rupees.

### Sample 3:
Input
Output

```
3 2
```

```
0

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-21T08:47:05.463Z  

```py
a,b=map(int,input().split())
if a>=b:
    print(0)
else:
    print(100)
```

---

[View on CodeChef](https://www.codechef.com/problems/P1235)