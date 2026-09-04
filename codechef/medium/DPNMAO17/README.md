# DPNMAO17

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Food for Rats

A group of rats is trying to survive in an area with several houses. You are given the number of rats, the amount of food each rat consumes, and an array $A$ denoting the amount of food available in each house.

Your task is to find the minimum number of houses you must visit, in order, to collect enough food for all the rats.

### Input Format
- The first line contains three space separated integers, $R$, $U$, and $N$ denoting the number of rats, the amount of food each rat consumes and size of the array.
- The second line contains $N$ space separated integers, representing the elements of the array $A$.
### Output Format
- A single integer representing the minimum number of houses required.
### Constraints
- $1 \leq R \leq 10^5$
- $1 \leq U \leq 10^4$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^4$
### Sample 1:
Input
Output

```
7 2 8
2 8 3 5 7 4 1 2
```

```
3
```

### Explanation:

Total food required = $R \times U = 7 \times 2 = 14$.
Food from house 2: $8$ Food from house 3: $3$ (Total collected: $8 + 3 = 11$)
Food from house 4: $5$ (Total collected: $11 + 5 = 16$)
The total food collected from the $3$ houses ($16$) is sufficient to feed all the rats ($14$).
Thus, the output is $3$.

### Sample 2:
Input
Output

```
10 3 5
1 2 3 4 5
```

```
0
```

### Explanation:
- Total food required = $10 \times 3 = 30$.
- Total food available in all houses = $1 + 2 + 3 + 4 + 5 = 15$.

Since the total available food is less than the required food, it's impossible to feed all the rats. Thus, the output is $0$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-04T17:33:32.848Z  

```py
import math

a,b,c=map(int,input().split())
nums=list(map(int,input().split()))
h=sum(nums)
g=a*b
if h>g:
    print(math.ceil(h/g))
else:
    print(0)
```

---

[View on CodeChef](https://www.codechef.com/problems/DPNMAO17)