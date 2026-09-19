# Cricket Average

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given two arrays of same size  **a[]** and  **b[]**, representing the runs scored by a player and their status ("out" or "notout") in each of the matches, find the player's batting average.

The average is defined as the total runs scored divided by the number of times the player got out, rounded up to the nearest integer (ceil value). If the player never got out across all matches, return -1.

 **Examples:** 

```
Input: a[] = [10, 101, 49], b[] = ["out", "notout", "out"]
Output: 80
Explanation: Total run = 10 + 101 + 49 = 160. The player gets out 2 times. So, average = 160 / 2 = 80.
```

```
Input: a[] = [15, 42, 20], b[] = ["out", "out", "notout"]
Output: 39
Explanation: Total run = 15 + 42 + 20 = 77. The player gets out 2 times. So, average = 77 / 2 = 38.5, which rounds up to 39.
```

 **Constraints:** 
1 ≤ a.size() = b.size() ≤ 500
1 ≤ a[i] ≤ 300
b[i] = "out" or b[i] = "notout"

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-19T13:44:18.161Z  

```py
import math

class Solution:

    def average(self, a, b):
        h=sum(a)
        g=b.count("out")
        if g==0:
            return -1
        else:
            return math.ceil(h/g)
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/cricket-average2031/1)