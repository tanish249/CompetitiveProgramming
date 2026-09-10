# STOCKMARKET - Rating 948

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Chef and Stocks

Chef has started learning about the stock market and has already selected a favourite stock.

He traded the stock for $N$ consecutive days. Let $A_i$ denotes the profit earned by Chef on the $i^{th}$ day.
Note that $A_i \lt 0$ indicates that Chef had a loss on the $i^{th}$ day.

Chef wants to find the  **maximum**  amount of of profit he would have earned, if he skipped trading for  **exactly one**  day.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input. The first line of each test case contains $N$ — the number of days. The next line denotes $N$ space-separated integers, denoting the profit earned by Chef on the $i^{th}$ day.
### Output Format

For each test case, output on a new line, the  **maximum**  amount of of profit he would have earned, if he skipped trading for  **exactly one**  day.

### Constraints
- $1 \leq T \leq 1000$
- $1 \leq N \leq 10^5$
- $-100 \leq A_i \leq 100$
- The sum of $N$ over all test cases won't exceed $10^6$.
### Sample 1:
Input
Output

```
4
3
1 -2 3
4
4 1 5 1
4
10 -10 -10 10
5
-5 -4 -3 -2 -1

```

```
4
10
10
-10

```

### Explanation:

 **Test case $1$:**  To make maximum profit, Chef would have skipped day $2$. The total profit for rest of the days is $1+3=4$.

 **Test case $2$:**  To make maximum profit, Chef would have skipped day $4$. The total profit for rest of the days is $1+4+5=10$.

 **Test case $3$:**  To make maximum profit, Chef would have skipped day $3$. The total profit for rest of the days is $10-10+10=10$.

 **Test case $4$:**  To make maximum profit, Chef would have skipped day $1$. The total profit for rest of the days is $-4-3-2-1=-10$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-10T14:03:07.389Z  

```py
t=int(input())
for _ in range(t):
    a=int(input())
    nums=list(map(int,input().split()))
    nums.sort()
    h=sum(nums)
    g=nums[0]
    print(h+g*-1)
```

---

[View on CodeChef](https://www.codechef.com/problems/STOCKMARKET)