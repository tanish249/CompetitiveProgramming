# TWOROOKS - Rating 957

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Two Rooks

You are given a standard $8 \times 8$ chessboard which has exactly $2$ rooks on it and no other pieces. The rows are numbered $1$ to $8$ from bottom to top, and the columns are numbered $1$ to $8$ from left to right. The cell at the intersection of the $i$-th column and $j$-th row is denoted $(i,j)$.

Given the initial positions of the rooks in the form of coordinates $(X_1,Y_1)$ and $(X_2,Y_2)$, you need to tell whether the $2$ rooks currently attack each other or not. Assume, each square can contain at most one piece.

Rooks can only travel in straight lines along the row or column they are placed at, and can't jump over other pieces. For a more detailed explanation of the moves of rooks, along with images, please click here.

### Input Format
- The first line contains $T$ - the number of test cases. Then the test cases follow.
- The first line of each test case contain four space-separated integers each $X_1, Y_1, X_2, Y_2$ - $(X_1,Y_1)$ is the position of the first rook and $(X_2,Y_2)$ is the position of the second rook.
### Output Format

For each test case, output on a single line `YES` (without quotes) if the rooks attack each other, and `NO` otherwise.

You may print each character of the string in uppercase or lowercase (for example, the strings `YeS`, `YEs`, `yes` and `yeS` will all be treated as identical).

### Constraints
- $1 \leq T \leq 5000$
- $1 \leq X_1, X_2, Y_1, Y_2 \leq 8$
- $(X_1,Y_1) \neq (X_2,Y_2)$
### Sample 1:
Input
Output

```
3
1 2 5 2
1 2 1 5
1 1 8 8

```

```
YES
YES
NO

```

### Explanation:
- Test case $1$: The two rooks can attack each other by moving along the second column.
- Test case $2$: The two rooks can attack each other by moving along the first row.
- Test case $3$: No matter how a rook moves it cannot reach the second rook in one move. Hence, they do not attack each other.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-11T15:46:35.353Z  

```py
t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    if a==c or b==d:
        print('YES')
    else:
        print('NO')
```

---

[View on CodeChef](https://www.codechef.com/problems/TWOROOKS)