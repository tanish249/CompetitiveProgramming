# FRIMEET - Rating 1098

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Friends Meetup

Chef and his friend is standing on the X-axis at the points $X_1$ and $X_2$ respectively.

Chef moves one step forward each second (that is he moves to $X_1 + 1$ after the $1^{st}$ second, $X_1 + 2$ after the $2^{nd}$ second, and so on), whereas his friend moves $2$ steps forward each second (that is he moves to $X_2 + 2$ after the $1^{st}$ second, $X_2 + 4$ after the $2^{nd}$ second, and so on).

You need to determine if Chef will be able to meet his friend or not. You can assume that Chef and his friend both keep on moving for a long indefinite amount of time and also that they move  **simultaneously**.

### Input Format
- The first line contains $T$ - the number of test cases. Then the test cases follow.
- The first line of each test case contain two space-separated integers $X_1$ and $X_2$ - the position of Chef and his friend at the start respectively.
### Output Format

For each test case, output on a single line `YES` (without quotes) if Chef can meet his friend, and `NO` otherwise.

You may print each character of the string in uppercase or lowercase (for example, the strings `YeS`, `YEs`, `yes` and `yeS` will all be treated as identical).

### Constraints
- $1 \leq T \leq 10^5$
- $1 \leq X_1, X_2 \leq 10^9$
### Sample 1:
Input
Output

```
3
1 1
1 7
7 1

```

```
YES
NO
YES
```

### Explanation:
- Test case $1$: Chef and his friend are on the same coordinate initially. Hence, they have already met.
- Test case $2$: No matter for how long they move Chef and his friend will never meet.
- Test case $3$: After $6$ seconds, Chef and his friend both will be at $X = 13$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-15T13:14:48.280Z  

```py
t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    if a>=b:
        print("YES")
    else:
        print("NO")
```

---

[View on CodeChef](https://www.codechef.com/problems/FRIMEET)