# FACEDIR - Rating 880

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Find the Direction

Chef is currently facing the north direction. Each second he rotates exactly $90$ degrees in clockwise direction. Find the direction in which Chef is facing after exactly $X$ seconds.

$\textbf{Note}:$ There are only 4 directions: North, East, South, West (in clockwise order).

### Input Format
- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of a single integer $X$.
### Output Format

For each testcase, output the direction in which Chef is facing after exactly $X$ seconds.

### Constraints
- $1 \leq T \leq 100$
- $1 \leq X \leq 1000$
### Sample 1:
Input
Output

```
3
1
3
6

```

```
East
West
South

```

### Explanation:

Chef is facing North in the starting.

 **Test Case $1$:**  After $1$ second he turns $90$ degrees clockwise and now faces the east direction.

 **Test Case $2$:**  Direction after $1$ second- east

Direction after $2$ seconds- south

Direction after $3$ seconds- west

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-15T08:26:44.559Z  

```py
t=int(input())
for _ in range(t):
    a=int(input())
    if a%4==0:
        print("North")
    elif a%4==2:
        print("South")
    elif a%4==1:
        print('East')
    else:
        print("West")
```

---

[View on CodeChef](https://www.codechef.com/problems/FACEDIR)