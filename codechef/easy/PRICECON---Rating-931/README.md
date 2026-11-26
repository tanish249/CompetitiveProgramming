# PRICECON - Rating 931

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Chef and Price Control

Chef has $N$ items in his shop (numbered $1$ through $N$); for each valid $i$, the price of the $i$-th item is $P_i$. Since Chef has very loyal customers, all $N$ items are guaranteed to be sold regardless of their price.

However, the government introduced a  *price ceiling*  $K$, which means that for each item $i$ such that $P_i \gt K$, its price should be reduced from $P_i$ to $K$.

Chef's  *revenue*  is the sum of prices of all the items he sells. Find the amount of revenue which Chef loses because of this price ceiling.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $K$.
- The second line contains $N$ space-separated integers $P_1, P_2, \ldots, P_N$.
### Output

For each test case, print a single line containing one integer ― the amount of lost revenue.

### Constraints
- $1 \le T \le 100$
- $1 \le N \le 10,000$
- $1 \le P_i \le 1,000$ for each valid $i$
- $1 \le K \le 1,000$
### Subtasks

 **Subtask #1 (100 points):**  original constraints

### Sample 1:
Input
Output

```
3
5 4
10 2 3 4 5
7 15
1 2 3 4 5 6 7
5 5
10 9 8 7 6
```

```
7
0
15
```

### Explanation:

 **Test Case 1** : The initial revenue is $10 + 2 + 3 + 4 + 5 = 24$. Because of the price ceiling, $P_1$ decreases from $10$ to $4$ and $P_5$ decreases from $5$ to $4$. The revenue afterwards is $4 + 2 + 3 + 4 + 4 = 17$ and the lost revenue is $24 - 17 = 7$.

 **Test Case 2** : The initial revenue is $1 + 2 + 3 + 4 + 5 + 6 + 7 = 28$. For each valid $i$, $P_i \le 15$, so there are no changes, the revenue after introduction of the price ceiling is the same and there is zero lost revenue.

 **Test Case 3** : The initial revenue is $10 + 9 + 8 + 7 + 6 = 40$. Since $P_i \gt 5$ for each valid $i$, the prices of all items decrease to $5$. The revenue afterwards is $5 \cdot 5 = 25$ and the lost revenue is $40 - 25 = 15$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-26T17:37:43.388Z  

```py
t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    nums=list(map(int,input().split()))
    h=sum(nums)
    ans=[]
    count =0
    for i in range(len(nums)):
        if b>=nums[i]:
            ans.append(nums[i])
        else:
            count +=1
    g=sum(ans)+count*b
    print(abs(h-g))
   
```

---

[View on CodeChef](https://www.codechef.com/problems/PRICECON)