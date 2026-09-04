# DPNMAO25

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Most Frequent Vowel

You are given a string $S$ of length $N$ consisting of lowercase English letters.
Your task is to find the vowel ($a$, $e$, $i$, $o$, $u$) that appears most frequently in the string.

 **Note:**  You may assume that the input string will always have a unique most frequent vowel.

### Input Format
- The first line contains a single integer $N$, representing the length of the string.
- The second line contains the string $S$.
### Output Format
- Print a single character representing the most frequent vowel.
### Constraints
- $1 \leq N \leq 10^5$
### Sample 1:
Input
Output

```
7
xayuaba
```

```
a
```

### Explanation:

The vowel $'a'$ occurs $3$ times, $'u'$ occurs $1$ time.
As $'a'$ occurs most frequently, it is our answer.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-04T17:25:00.562Z  

```py
t=int(input())
p=input()
q=p.count("a")
w=p.count("e")
e=p.count("i")
r=p.count("o")
t=p.count("u")
o=max(q,w,e,r,t)
if o==q:
    print('a')
elif o==w:
    print('e')
elif o==e:
    print('i')
elif o==r:
    print("o")
else:
    print("u")
```

---

[View on CodeChef](https://www.codechef.com/problems/DPNMAO25)