# DPNMAO15

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Merge Sorted Arrays

Two rival e-commerce platforms have decided to merge. For a specific category, each platform provides a list of its product IDs, which are already sorted in ascending order.
Your task is to combine these two lists into a single, sorted list of product IDs to create a unified catalog.

### Input Format
- The first line contains two space separated integers, $N$ and $M$, representing the number of elements in the first and second arrays, respectively.
- The second line contains $N$ space separated integers, representing the elements of the first array.
- The third line contains $M$ space separated integers, representing the elements of the second array.
### Output Format
- Print the merged and sorted list of integers, with each element separated by a space.
### Constraints
- $1 \leq N, M \leq 10^5$
### Sample 1:
Input
Output

```
5 5
1 2 3 4 5
2 4 6 8 10
```

```
1 2 2 3 4 4 5 6 8 10
```

### Sample 2:
Input
Output

```
4 6
10 20 30 40
5 15 25 35 45 55
```

```
5 10 15 20 25 30 35 40 45 55
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-05T09:34:40.341Z  

```py
a,b=map(int,input().split())
num1=list(map(int,input().split()))
num2=list(map(int,input().split()))
nums=num1+num2
nums.sort()
print(*nums)
```

---

[View on CodeChef](https://www.codechef.com/problems/DPNMAO15)