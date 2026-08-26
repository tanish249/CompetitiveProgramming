# SOLBLTY - Rating 922

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Solubility

Suppose for a unit rise in temperature, the solubility of sugar in water increases by $B \frac{\mathrm{g}}{100\ \mathrm{mL}}$.

Chef does an experiment to check how much sugar (in $\mathrm{g}$) he can dissolve given that he initially has $1$ liter of water at $X$ degrees and the solubility of sugar at this temperature is $A \frac{\mathrm{g}}{100\ \mathrm{mL}}$. Also, Chef doesn't want to lose any water so he can increase the temperature to at most $100$ degrees.

Assuming no loss of water takes place during the process, find the maximum amount of sugar (in $\mathrm{g}$) can be dissolved in $1$ liter of water under the given conditions.

###Input

- The first line contains an integer $T$, the number of test cases. Then the test cases follow.
- The only line of each test case contains three integers $X, A, B$.

###Output For each testcase, output in a single line the answer to the problem.

###Constraints

- $1 \leq T \leq 1000$
- $31 \leq X \leq 40$
- $101 \leq A \leq 120$
- $1 \leq B \leq 5$

###Subtasks  **Subtask #1 (100 points):**  Original Constraints

### Sample 1:
Input
Output

```
3
40 120 1
35 120 2
40 115 3
```

```
1800
2500
2950
```

### Explanation:

 **Test Case $1$:**  Since solubility is increasing with temperature, the maximum solubility will be at $100$ degrees which is equal to $120 + (100 - 40) = 180 \frac{\mathrm{g}}{100\ \mathrm{mL}}$.

So for $1$ liter of water the value is $180 \cdot 10 = 1800\ \mathrm{g}$.

 **Test Case $2$:**  Since solubility is increasing with temperature, the maximum solubility will be at $100$ degrees which is equal to $120 + (100 - 35) \cdot 2 = 250\frac{\mathrm{g}}{100\ \mathrm{mL}}$.

So for $1$ liter of water the value is $250 \cdot 10 = 2500\ \mathrm{g}$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-26T05:55:10.879Z  

```py
t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    h=b+(100-a)*c
    print(h*10)
```

---

[View on CodeChef](https://www.codechef.com/problems/SOLBLTY)