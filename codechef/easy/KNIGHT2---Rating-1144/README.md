# KNIGHT2 - Rating 1144

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Journey of the Knight

Chef has an $8 \times 8$ chessboard. He placed a knight on the square $(X_1, Y_1)$. Note that, the square at the intersection of the $i^{th}$ row and $j^{th}$ column is denoted by $(i, j)$.

Chef wants to determine whether the knight can end up at the square $(X_2, Y_2)$ in  **exactly**  $100$ moves or not.

For reference, a knight can move to a square which is:

- One square horizontally and two squares vertically away from the current square, or
- One square vertically and two squares horizontally away from the current square

A visual description of this may be found here.

### Input Format
- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains $4$ integers $X_1, Y_1, X_2, Y_2$ — where $(X_1, Y_1)$ denotes the starting square of the knight and $(X_2, Y_2)$ denotes the ending square of the knight.
### Output Format

For each test case, output `YES` if knight can move from $(X_1, Y_1)$ to $(X_2, Y_2)$ in  **exactly**  $100$ moves. Otherwise, output `NO`.

You may print each character of `YES` and `NO` in uppercase or lowercase (for example, `yes`, `yEs`, `Yes` will be considered identical).

### Constraints
- $1 \leq T \leq 1000$
- $1 \le X_1, Y_1, X_2, Y_2 \le 8$
### Sample 1:
Input
Output

```
3
1 1 1 1
8 8 7 6
8 8 8 6

```

```
YES
NO
YES
```

### Explanation:

 **Test Case 1:**  Knight can first move to $(2, 3)$ and then back to $(1, 1)$. He can repeat this $50$ times and he will end up at $(1, 1)$ after $100$ moves.

 **Test Case 2:**  It can be proven that it is not possible for the knight to end at $(7, 6)$ after $100$ moves.

 **Test Case 3:**  Knight can first move to $(6, 7)$ and then to $(8, 6)$. After that, he can alternate between $(6, 7)$ and $(8, 6)$ for $49$ times and he will end up at $(8, 6)$ after $100$ moves.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-06T08:25:58.845Z  

```py
t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    h=abs(a-c)
    g=abs(b-d)
    if h==0 or g==0:
        print("YES")
    else:
        print("NO")
```

---

[View on CodeChef](https://www.codechef.com/problems/KNIGHT2)