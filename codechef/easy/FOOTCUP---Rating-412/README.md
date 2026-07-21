# FOOTCUP - Rating 412

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Football Cup

It is the final day of La Liga. Chef has a certain criteria for assessing football matches.
In particular, he only likes a match if:

- The match ends in a draw, and,
- At least one goal has been scored by either team.

Given the goals scored by both the teams as $X$ and $Y$ respectively, determine whether Chef will like the match or not.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- Each test case consists of a single line of input containing two space-separated integers $X$ and $Y$ — the goals scored by each team.
### Output Format

For each test case, output $\texttt{YES}$ if Chef will like the match, else output $\texttt{NO}$.

You may print each character of the string in uppercase or lowercase (for example, the strings $\texttt{YeS}$, $\texttt{yEs}$, $\texttt{yes}$ and $\texttt{YES}$ will all be treated as identical).

### Constraints
- $1 \leq T \leq 100$
- $0 \leq X, Y \leq 9$
### Sample 1:
Input
Output

```
4
1 1
0 1
0 0
2 2

```

```
YES
NO
NO
YES
```

### Explanation:

 **Test case $1$:**  It is a draw in which both teams have scored a goal, Chef will like this match.

 **Test case $2$:**  The game is not a draw. Hence, Chef will not like this match.

 **Test case $3$:**  Neither team scored a goal, so Chef will not like this match.

 **Test case $4$:**  It is a draw in which both teams scored $2$ goals each. Chef will like this match.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-21T13:10:53.713Z  

```py
t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=a+b
    if a==b and h>0 :
        print("YES")
    else:
        print("NO")
```

---

[View on CodeChef](https://www.codechef.com/problems/FOOTCUP)