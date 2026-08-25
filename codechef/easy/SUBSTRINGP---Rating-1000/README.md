# SUBSTRINGP - Rating 1000

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Check if a string is a substring of another

Given two strings, `S1` and `S2`, your task is to determine whether `S2` is a substring of `S1`. If `S2` is a substring of `S1`, print "YES". Otherwise, print "NO".

A substring is a contiguous sequence of characters within a string. For example, "abc" is a substring of "aabcda", but "ac" is not a contiguous sequence in "aabcda".

### Input Format
- The first line contains a single integer T, the number of test cases.
- Each test case consists of two lines: The first line contains the string S1. The second line contains the string S2.
### Output Format

For each test case, print a single line containing either "YES" or "NO", depending on whether `S2` is a substring of `S1`.

### Constraints
- $1 \leq T \leq 100$
- $1 \leq |S1|, |S2| \leq 1000$
- S1 and S2 contain only lowercase English letters.
### Sample 1:
Input
Output

```
4
hello
ell
codechef
chef
programming
debug
abcd
efgh

```

```
YES
YES
NO
NO

```

### Explanation:
- In the first test case, "ell" is a substring of "hello".
- In the second test case, "chef" is a substring of "codechef".
- In the third test case, "debug" is not a substring of "programming".
- In the fourth test case, "efgh" is not a substring of "abcd".

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-25T08:15:59.620Z  

```py
t=int(input())
for _ in range(t):
    a=input()
    b=input()
    if b in a:
        print("YES")
    else:
        print("NO")
```

---

[View on CodeChef](https://www.codechef.com/problems/SUBSTRINGP)