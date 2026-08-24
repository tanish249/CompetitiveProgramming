# FBMATCH - Rating 632

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Front-Back Matching

You are given a string $S$ of length $N$.
The string contains only lowercase English letters.

You can freely rearrange the characters of $S$ however you like.

After rearrangement, is it possible to make the first and last characters of $S$ equal?

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input. The first line of each test case contains a single integer $N$ — the length of string $S$. The second line contains the string $S$ of length $N$.
### Output Format

For each test case, output on a new line the answer: either $\tt{Yes}$ or $\tt{No}$, depending on whether it's possible to rearrange the string appropriately or not.

Each character of the output may be printed in either uppercase or lowercase, for example the strings $\tt{yes}, \tt{YES}, \tt{yES}$ will all be accepted if valid rearrangements exist.

### Constraints
- $1 \leq T \leq 100$
- $2 \leq N \leq 100$
- $S$ contains only lowercase English letters, i.e. $S_i \in \{\tt{a,b,}\ldots, \tt{z}\}$.
### Sample 1:
Input
Output

```
4
3
aka
4
nope
5
pluto
5
foggy

```

```
Yes
No
No
Yes
```

### Explanation:

 **Test case $1$:**  $S = \tt{aka}$, so its first and last characters are already equal.

 **Test case $4$:**  $S = \tt{foggy}$, and it can be rearranged to obtain $S = \tt{gyfog}$ which has equal first and last characters.

In test cases $2$ and $3$, it can be proved that no rearrangement of the given string has equal first and last characters.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-24T16:17:42.424Z  

```py
t=int(input())
for _ in range(t):
    a=int(input())
    x=input()
    h=max(x, key=x.count)
    p=(x.count(h))
    if p>=2:
        print('YES')
    else:
        print("NO")
```

---

[View on CodeChef](https://www.codechef.com/problems/FBMATCH)