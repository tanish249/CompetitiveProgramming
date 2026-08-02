# CHEAPFUEL - Rating 926

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Which Fuel is Cheaper

The current price of petrol is $X$ rupees, and the current price of diesel is $Y$ rupees. At the start of each month, the price of petrol increases by $A$ rupees and the price of diesel increases by $B$ rupees.

Chef is curious to know which fuel costs less at the end of the $K^{th}$ month. If petrol is cheaper than diesel at the end of $K^{th}$ month, then print $\verb+PETROL+$. If diesel is cheaper than petrol at the end of the $K^{th}$ month, then print $\verb+DIESEL+$. If both the fuels have the same price at the end of the $K^{th}$ month, then print $\verb+SAME PRICE+$.

### Input Format
- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- Each test case consists of a single line of input, containing five space-separated integers $X, Y, A, B, K$.
### Output Format

For each test case,

- Print $\verb+PETROL+$ if petrol is cheaper than diesel.
- Print $\verb+DIESEL+$ if diesel is cheaper than petrol.
- Print $\verb+SAME PRICE+$ otherwise.

 **Note:**  The output is case-insensitive. You can print each character in either lower-case or upper-case.

### Constraints
- $1 \leq T \leq 1000$
- $1 \leq K \leq 1000$
- $0 \leq X, Y, A, B \leq 1000$
### Subtasks
- Subtask 1 (100 points): Original constraints
### Sample 1:
Input
Output

```
3
1 1 1 1 1
2 1 2 1 2
2 2 1 1 2

```

```
SAME PRICE
DIESEL
SAME PRICE

```

### Explanation:

 **Test case 1:** 

Initially, the price of petrol is $1$ rupee and the price of diesel is $1$ rupee. Since $A = 1$ and $B = 1$, the prices of both petrol and diesel increase by $1$ rupee at the start of every month. So, at the start of the first month, the price of petrol becomes $1 + 1 = 2$ rupees and the price of diesel becomes $1 + 1 = 2$ rupees. By the end of the first month, the price of petrol and diesel are both $2$ rupees and hence they both have the same price.

 **Test case 2:** 

Initially, the price of petrol is $2$ rupees and the price of diesel is $1$ rupee. Since $A = 2$ and $B = 1$, the price of petrol increases by $2$ rupee and the price of diesel increases by $1$ rupee at the start of every month. It follows that at the start of the first month, the price of petrol becomes $2 + 2 = 4$ rupees and the price of diesel becomes $1 + 1 = 2$ rupees. And by the start of the second month, the price of petrol becomes $4 + 2 = 6$ rupees and the price of diesel becomes $2 + 1 = 3$ rupees. By the end of the second month, the prices of petrol and diesel are $6$ rupees and $3$ rupees respectively and hence diesel is cheaper than petrol.

 **Test case 3:** 

Initially, the price of petrol is $2$ rupee and the price of diesel is $2$ rupee. Since $A = 1$ and $B = 1$, the price of petrol increases by $1$ rupee and the price of diesel increases by $1$ rupee at the start of every month. It follows that at the start of the first month, the price of petrol becomes $2 + 1 = 3$ rupees and the price of diesel becomes $2 + 1 = 3$ rupees. And by the start of the second month, the price of petrol becomes $3 + 1 = 4$ rupees and the price of diesel becomes $3 + 1 = 4$ rupees. By the end of the second month, the prices of petrol and diesel are both $4$ rupees and hence both have the same prices.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-02T09:20:35.317Z  

```py
t=int(input())
for _ in range(t):
    a,b,c,d,e=map(int,input().split())
    h=e*c
    g=e*d
    o=a+h
    p=b+g
    if o==p:
        print("SAME PRICE")
    elif o>p:
        print('DIESEL')
    else:
        print("PETROL")
```

---

[View on CodeChef](https://www.codechef.com/problems/CHEAPFUEL)