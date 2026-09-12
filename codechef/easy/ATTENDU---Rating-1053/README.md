# ATTENDU - Rating 1053

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Minimum Attendance Requirement

A semester in Chef's University has $120$ working days. The University's requirement is that a student should be present for at least $75\%$ of the working days in the semester. If not, the student is failed.

Chef has been taking a lot of holidays, and is now concerned whether he can pass the attendance requirement or not. $N$ working days have already passed, and you are given $N$ bits - $B_1$, $B_2$,..., $B_N$. $B_i$ = $0$ denotes that Chef was absent on the $i^{th}$ day, and $B_i$ = $1$ denotes that Chef was present on that day.

Can Chef hope to pass the requirement by the end of the semester?

###Input:

- First line will contain $T$, the number of testcases. Then the testcases follow.
- Each testcase contains two lines of input.
- The first line of each testcase contains a single integer, $N$, the number of days till now.
- The second line of each testcase contains a string $B$ of length $N$ where $B_i$ represents the status of the $i^{th}$ day.

###Output: For each testcase, output the answer in a single line - "YES" if Chef can pass the attendance requirement and "NO" if not.

###Constraints

- $1 \leq T \leq 10$
- $1 \leq N \leq 120$
- $0 \leq B_i \leq 1$
### Sample 1:
Input
Output

```
3
50
00000000000000000000000000000000000000000000000000
50
01010101010101010101010101010101010101010101010101
2
01
```

```
NO
YES
YES
```

### Explanation:

For Case 1, even if Chef attends all the remaining 70 days, he'll only have an attendance percentage of $70/120$ = $58.33\%$ which is less than $75\%$.

For Case 2, maximum attendance possible is $79.167\%$ which is more than $75\%$.

For Case 3, maximum attendance possible is $99.167\%$ which is more than $75\%$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-12T08:37:39.687Z  

```py
t=int(input())
for _ in range(t):
    a=int(input())
    x=input()
    h=x.count("1")
    f=abs(120-a)
    u=h+f
    y=(u/120)*100
    if y>=75.00:
        print('YES')
    else:
        print('NO')
    
    
```

---

[View on CodeChef](https://www.codechef.com/problems/ATTENDU)