# CHANGE_PLZ - Rating 760

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Change Please

You just travelled in a cab and you owe the driver $X$ dollars.
However, you only have a $100$ dollar bill, and the driver only has $10$ dollar bills with which he can pay you back.

You hand the $100$ dollar bill to the driver. Find the  **maximum**  amount which the driver can pay back without giving more than he owes.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single integer $X$, the amount you owe the driver.
### Output Format

For each test case, output on a new line, the  **maximum**  amount which driver can pay back without giving more than he owes.

### Constraints
- $1 \leq T \leq 100$
- $1 \leq X \leq 100$
### Sample 1:
Input
Output

```
3
90
100
66

```

```
10
0
30
```

### Explanation:

 **Test case $1$:**  Driver pays back the remaining $100-90=10$ dollars in form a $10$ dollar bill.

 **Test case $2$:**  Driver does not pay back any money since the fare is $100$.

 **Test case $3$:**  After receiving $100$ dollar bill, driver owes you $100-66 = 34$ dollars. Driver gives back three $10$ dollars bills.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-06T14:42:25.650Z  

```py
t=int(input())
for _ in range(t):
    a=int(input())
    h=100-a
    print(h-(h%10))
```

---

[View on CodeChef](https://www.codechef.com/problems/CHANGE_PLZ)