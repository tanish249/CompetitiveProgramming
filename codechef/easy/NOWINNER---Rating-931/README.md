# NOWINNER - Rating 931

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### No Winner

After a series of matches between Alice, Bob, and Cameron, their scores are $A$, $B$, and $C$, respectively.
Chef plans to organise $M$ additional matches. In each match,  **two**  players compete, and there is exactly one winner.
The winner of the match receives one point.

Determine if it is possible for  **at least**  two players to end up with the same score after all $M$ additional matches have been completed.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case contains four space-separated integers $A, B, C$ and $M$ — the initial scores of Alice, Bob, and Cameron, and the number of additional matches, respectively.
### Output Format

For each test case, output on a new line the answer: `YES`, if it is possible for  **at least**  two players to end up with the same score after these $M$ matches, and `NO` otherwise.

You may print each character of the string in uppercase or lowercase (for example, the strings `YES`, `yEs`, `yes`, and `yeS` will all be treated as identical).

### Constraints
- $1 \leq T \leq 10^4$
- $1 \leq A, B, C, M \leq 10$
### Sample 1:
Input
Output

```
3
3 5 2 1
4 4 2 5
1 4 7 2

```

```
YES
YES
NO

```

### Explanation:

 **Test case $1$:**  Consider the scenario where the additional match is held between Alice and Cameron, and Cameron wins. Thus, final scores would be $3, 5,$ and $3$ respectively.

 **Test case $2$:**  Consider the scenario where all the additional matches are held between Bob and Cameron, and Cameron wins all of them. Thus, final scores would be $4, 4,$ and $7$ respectively.

 **Test case $3$:**  It can be shown that the final scores cannot be same for any two players.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-16T08:22:51.608Z  

```py
t=int(input())
for _ in range(t):
    nums=list(map(int,input().split()))
    h=sum(nums)
    if h%2==0:
        print("NO")
    else:
        print("YES")
```

---

[View on CodeChef](https://www.codechef.com/problems/NOWINNER)