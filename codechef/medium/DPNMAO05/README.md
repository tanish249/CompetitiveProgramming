# DPNMAO05

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Peak Elevation

A hiker is trekking through a mountain range. During the trek, they record their elevation at various points. The sequence of recorded elevations first increases and then may decrease, forming a shape similar to a mountain.
Your task is to find the highest elevation point the hiker reached. This highest point is called the "elevation point" or the peak of the trek.

Given a sequence of elevations, find the maximum elevation.

### Input Format
- The first line contains an integer $N$, representing the number of elevation recordings.
- The second line contains $N$ space separated integers, $A_0, A_1,..., A_\text{N-1}$, representing the elevations.
### Output Format
- Print a single integer which is the maximum elevation in the given sequence.
### Constraints
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
### Sample 1:
Input
Output

```
7
1 2 3 4 3 2 1
```

```
4
```

### Explanation:

4 is the highest elevation point.

### Sample 2:
Input
Output

```
2
5 3
```

```
5
```

### Explanation:

The highest elevation is 5.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-05T09:33:43.530Z  

```py
a=int(input())
nums=list(map(int,input().split()))
print(max(nums))
```

---

[View on CodeChef](https://www.codechef.com/problems/DPNMAO05)