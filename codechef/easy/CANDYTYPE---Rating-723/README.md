# CANDYTYPE - Rating 723

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Candy Types

The candies in this universe come in $N$ colours, numbered $1$ to $N$.

You have $N$ candies with you, the $i$-th candy having a colour $A_i$.

You wonder what is the most frequent colour among your candies. In case there is a tie, you should print the smaller colour among all the most frequent colours.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input. The first line contains a single integer $N$. The second line contains $N$ integers - $A_1, A_2, \ldots, A_N$.
### Output Format

For each test case, output on a new line the most frequent colour of your candies.

### Constraints
- $1 \le T \le 100$
- $1 \le N \le 100$
- $1 \le A_i \le N$
### Sample 1:
Input
Output

```
3
3
1 2 3
3
3 3 3
5
3 3 4 4 1

```

```
1
3
3

```

### Explanation:

 **Test Case 1**  : All the candy colours from $1$ to $3$ appear exactly once, but we should print the smallest one, which is $1$.

 **Test Case 2**  : Only candy colour $3$ appears, hence it is the most frequent.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-08T14:07:09.435Z  

```py
t=int(input())
for _ in range(t):
    a=int(input())
    nums=list(map(int,input().split()))
    nums.sort()
    h=max(nums,key=nums.count)
    print(h)
```

---

[View on CodeChef](https://www.codechef.com/problems/CANDYTYPE)