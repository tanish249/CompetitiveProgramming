# HATTRICK - Rating 853

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Hattrick

In a cricket match, the retiring of three batsmen with  **three consecutive**  balls is termed as a  *hattrick*.

Let $A, B, C, D, E,$ and $F$ denote the batsman's score for each ball in order in an over.
Each of these variables can be an integer less than equal to $6$ denoting the runs scored by the batsman, or `W` denoting a wicket.

Find whether there was a hattrick in this over.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of six space-separated integers (or 'W') $A, B, C, D, E, F$, denoting the batsman's score for each ball in the over.
### Output Format

For each test case, output on a new line, `YES`, if there was a hattrick in the over, and `NO` otherwise.

You may print each character of the string in uppercase or lowercase (for example, the strings $\texttt{YeS}$, $\texttt{yEs}$, $\texttt{yes}$ and $\texttt{YES}$ will all be treated as identical).

### Constraints
- $1 \leq T \leq 5\cdot 10^4$
- $A, B, C, D, E, F \in \{0, 1, 2, 4, 6,$W$\}$
### Sample 1:
Input
Output

```
4
1 2 W 0 W 6
W W W 6 6 6
W 4 W 0 W 6
1 W W W W 0

```

```
NO
YES
NO
YES

```

### Explanation:

 **Test case $1$:**  Wickets were not taken for $3$ consecutive balls. Thus, there was no hattrick.

 **Test case $2$:**  Wickets were taken for first $3$ consecutive balls. Thus, there was a hattrick.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-30T10:31:34.764Z  

```py
t=int(input())
for _  in range(t):
    a=list(map(str,input().split()))
    h=a[0]+a[1]+a[2]
    g=a[3]+a[4]+a[5]
    j=a[1]+a[2]+a[3]
    k=a[2]+a[3]+a[4]
    if h=="WWW"or g=="WWW" or j=="WWW" or k=="WWW":
        print("YES")
    else:
        print("NO")
```

---

[View on CodeChef](https://www.codechef.com/problems/HATTRICK)