# LOCKDRAW - Rating 982

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Chef and Lockout Draws

Bob and Alice are having a lockout match between them. There are three problems in the contest worth $A$, $B$, and $C$ points respectively. Only the first player to solve a problem gets points for that problem. It is impossible for Bob and Alice to solve a problem at the same time. Chef wants to know if there is any chance of a draw if Bob and Alice manage to solve all $3$ problems. A draw occurs when both players end with equal number of points.

### Input Format
- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of a single line of input, three space separated integers $A$, $B$, and $C$.
### Output Format

For each testcase, output YES if the match can end in a draw, and NO otherwise.

You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

### Constraints
- $1 \leq T \leq 1000$
- $1 \leq A, B, C \leq 10^6$
### Subtasks

 **Subtask #1 (100 points):**  original constraints

### Sample 1:
Input
Output

```
3
2 5 2
4 2 2
3 5 5
```

```
NO
YES
NO
```

### Explanation:

In the first and third test cases, it is impossible for Bob and Alice to solve the problems so that they have the same number of points at the end.

In the second case, it is possible for Bob to solve the first problem, and Alice to solve the last two problems, in which case they will both have 4 points and the game will end in a draw.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-13T05:55:21.581Z  

```py
t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    h=a+b
    g=a+c
    f=b+c
    if h==c or g==b or f==a:
        print("YES")
    else:
        print("NO")
```

---

[View on CodeChef](https://www.codechef.com/problems/LOCKDRAW)