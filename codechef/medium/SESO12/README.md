# SESO12

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Sort three integer

You are tasked with sorting a 3-integer array manually, without using any built-in sorting functions or libraries. Implement a program that reads three integers from input and rearranges them in ascending order.

### Input Format:
- Three integers separated by spaces on a single line.
### Output Format:
- Print the three integers in ascending order, separated by spaces.
### Sample 1:
Input
Output

```
5 2 7

```

```
2 5 7
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-08T14:32:42.473Z  

```py
nums=list(map(int,input().split()))

n=len(nums)

for i in range(n):
    for j in range(n-1-i):
        if nums[j] > nums[j+1]:
           nums[j] , nums[j+1] = nums[j+1] , nums[j]
print(*nums)
    
```

---

[View on CodeChef](https://www.codechef.com/problems/SESO12)