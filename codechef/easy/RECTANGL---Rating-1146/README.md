# RECTANGL - Rating 1146

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Rectangle

You are given four integers  **a**,  **b**,  **c**  and  **d**. Determine if there's a rectangle such that the lengths of its sides are  **a**,  **b**,  **c**  and  **d**  (in any order).

### Input

- The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
- The first and only line of each test case contains four space-separated integers a, b, c and d.

### Output

For each test case, print a single line containing one string "YES" or "NO".

### Constraints
- 1 ≤ T ≤ 1,000
- 1 ≤ a, b, c, d ≤ 10,000
### Subtasks

 **Subtask #1 (100 points):**  original constraints

### Sample 1:
Input
Output

```
3
1 1 2 2
3 2 2 3
1 2 2 2
```

```
YES
YES
NO
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-06T08:43:02.281Z  

```py
t=int(input())
for _ in range(t):
    nums=list(map(int,input().split()))
    nums.sort()
    if nums[3]==nums[2] and nums[0]==nums[1]:
        print('YES')
    else:
        print("NO")
```

---

[View on CodeChef](https://www.codechef.com/problems/RECTANGL)