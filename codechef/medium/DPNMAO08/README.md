# DPNMAO08

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Large Small Sum

You are a data analyst working with a sequence of numerical data. Your task is to perform a specific calculation on this data.

You are given an array $A$. Your task is to find the sum of the second largest element among the numbers at the even positions and the second smallest element among the numbers at odd positions in the array. If $N \le 3$, or if either list does not have enough elements to determine the required value, print `0`.

### Input Format
- The first line contains an integer $N$, representing the size of the array.
- The second line contains $N$ space separated integers, representing the elements of the array $A$.
### Output Format
- Print a single integer representing the calculated sum.
### Constraints
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
### Sample 1:
Input
Output

```
6
3 2 1 7 5 4
```

```
7
```

### Explanation:

The elements at even positions (0, 2, 4) are $3, 1, 5$. The second largest among these is $3$.
The elements at odd positions (1, 3, 5) are $2, 7, 4$. The second smallest among these is $4$.
The required sum is $3 + 4 = 7$.

### Sample 2:
Input
Output

```
7
1 8 0 2 3 5 6
```

```
8
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-04T17:29:57.550Z  

```py
a=int(input())
nums=list(map(int,input().split()))
print(max(nums))
```

---

[View on CodeChef](https://www.codechef.com/problems/DPNMAO08)