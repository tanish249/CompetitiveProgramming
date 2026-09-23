# ADD13 - Rating 1003

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Add 1 or 3

You start with an integer $X = 0$. For $N$ turns, you do  **exactly one**  of the following:

- Either, you add $1$ to $X$
- Or, you add $3$ to $X$

For example, for $N = 2$, you can choose to add $1$ on the first turn, and $3$ on the second turn, thus a final value of $X = 4$.

Given an integer $M$, print whether it is possible that the final value of $X$ is $M$ or not.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case contains $2$ integers - $N$ and $M$.
### Output Format

For each test case, output on a new line $\text{YES}$ if it possible to form $M$ with exactly $N$ turns, and $\text{NO}$ otherwise.

It is allowed to print each character in either case, $\text{Yes}$, $\text{yes}$ and $\text{yEs}$ will all be accepted as positive responses.

### Constraints
- $1 \le T \le 1000$
- $1 \le N, M \le 10^9$
### Sample 1:
Input
Output

```
11
1 1
1 2
1 3
2 2
2 4
2 5
2 6
2 8
3 1
9 23
10 23

```

```
YES
NO
YES
YES
YES
NO
YES
NO
NO
YES
NO
```

### Explanation:

 **Test Case 1, 2, 3**  : In one turn, you can add $1$ or $3$, thus obtaining either $X = 1$ or $X = 3$. Hence, $M = 1$ and $M = 3$ are achievable but not $M = 2$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-23T15:17:54.920Z  

```py
# cook your dish here

```

---

[View on CodeChef](https://www.codechef.com/problems/ADD13)