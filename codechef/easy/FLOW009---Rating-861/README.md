# FLOW009 - Rating 861

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Total Expenses

While purchasing certain items, a discount of 10% is offered if the quantity purchased is more than 1000.
If the quantity and price per item are input, write a program to calculate the total expenses.

### Input Format

The first line contains an integer  **T**, total number of test cases. Then follow  **T**  lines, each line contains integers  **quantity**  and  **price**.

### Output Format

For each test case, output the total expenses while purchasing items, in a new line.

### Constraints
- 1 ≤ T ≤ 1000
- 1 ≤ quantity,price ≤ 100000
### Sample 1:
Input
Output

```
3 
100 120
10 20
1200 20

```

```
12000.000000
200.000000
21600.000000

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-02T07:27:34.321Z  

```py
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    g = a * b
    h = 10 * g / 100

    if a > 1000:
        print(f"{g - h:.6f}")
    else:
        print(f"{g:.6f}")
```

---

[View on CodeChef](https://www.codechef.com/problems/FLOW009)