# CRICRANK - Rating 966

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Cricket Ranking

In a season, each player has three statistics: runs, wickets, and catches. Given the season stats of two players $A$ and $B$, denoted by $R$, $W$, and $C$ respectively, the person who is better than the other in the most statistics is regarded as the better overall player. Tell who is better amongst $A$ and $B$. It is known that in each statistic, the players have different values.

### Input Format
- The first line contains an integer $T$, the number of test cases. Then the test cases follow.
- Each test case contains two lines of input.
- The first line contains three integers $R_1$, $W_1$, $C_1$, the stats for player $A$.
- The second line contains three integers $R_2$, $W_2$, $C_2$, the stats for player $B$.
### Output Format

For each test case, output in a single line `"A"` (without quotes) if player $A$ is better than player $B$ and `"B"` (without quotes) otherwise.

### Constraints
- $1 \leq T \leq 1000$
- $0 \leq R_1, R_2 \leq 500$
- $0 \leq W_1, W_2 \leq 20$
- $0 \leq C_1, C_2 \leq 20$
- $R_1 \neq R_2$
- $W_1 \neq W_2$
- $C_1 \neq C_2$
### Sample 1:
Input
Output

```
3
0 1 2
2 3 4
10 10 10
8 8 8
10 0 10
0 10 0
```

```
B
A
A
```

### Explanation:

 **Test Case $1$:**  Player $B$ is better than $A$ in all $3$ fields.

 **Test Case $2$:**  Player $A$ is better than $B$ in all $3$ fields.

 **Test Case $3$:**  Player $A$ is better than $B$ in runs scored and number of catches.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-10T14:13:29.582Z  

```py
t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    x,y,z=map(int,input().split())
    if a> x and c>z:
        print("A")
    elif b>y and c>z:
        print("A")
    elif a>x and b>y:
        print("A")
    else:
        print("B")
```

---

[View on CodeChef](https://www.codechef.com/problems/CRICRANK)