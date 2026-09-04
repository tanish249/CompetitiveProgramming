# DPNMAO02

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Anagram Check

You are given two strings, $S$ and $T$. Your task is to determine if it's possible to rearrange the characters of $S$ to form the string $T$. In other words, you need to check if $T$ is an anagram of $S$.

 **NOTE:**  An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

### Input Format
- The first line of input contains the string $S$.
- The second line of input contains the string $T$.
### Output Format
- Print True if $T$ can be formed by rearranging the characters of $S$, otherwise print False.
### Constraints
- $1\leq |S|, |T| \leq 1000$
- The strings consist of lowercase English letters only.
### Sample 1:
Input
Output

```
listen
silent
```

```
true
```

### Sample 2:
Input
Output

```
hello
world
```

```
false
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-04T16:21:24.650Z  

```py
a=input()
b=input()
h=list(sorted(a))
g=list(sorted(b))
if h==g:
    print("true")
else:
    print("false")
```

---

[View on CodeChef](https://www.codechef.com/problems/DPNMAO02)