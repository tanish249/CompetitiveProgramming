# PREP17 - Rating 1100

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Maximum Common Elements

Given two arrays $A$ and $B$, each of size $N$, where each array consists of  **distinct**  elements.

Find the number of elements that are common in both the arrays.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input. The first line of each test case contains an integer $N$ — the size of both the arrays. The second line contains $N$ space separated integers - the elements of array $A$. The third line contains $N$ space separated integers - the elements of array $B$.
### Output Format

For each test case, output on a new line, the number of elements that are common in both the arrays.

### Constraints
- $1 \leq T \leq 100$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$, the values $A_i$ are distinct.
- $1 \leq B_i \leq 10^9$, the values $B_i$ are distinct.
- The sum of $N$ over all test cases won't exceed $2\cdot 10^5$.
### Sample 1:
Input
Output

```
3
4
1 2 3 4
1 3 4 5
3
2 4 1
1 4 2
1
2
3

```

```
3
3
0

```

### Explanation:

 **Test case $1$:**  There are $3$ common elements in both the arrays, which are, $1, 3,$ and $4$.

 **Test case $2$:**  There are $3$ common elements in both the arrays, which are, $1, 2,$ and $4$.

 **Test case $3$:**  There are no common elements between both arrays.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-12T07:52:12.035Z  

```py
t=int(input())
for _ in range(t):
    a=int(input())
    num1=list(map(int,input().split()))
    num2=list(map(int,input().split()))
    h=num1+num2
    o=len(h)
    p=len(set(h))
    print(abs(o-p))
```

---

[View on CodeChef](https://www.codechef.com/problems/PREP17)