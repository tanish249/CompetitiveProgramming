# PASSTHEEXAM - Rating 424

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Pass the Exam

Chef appeared for an exam consisting of $3$ sections. Each section is worth $100$ marks.

Chef scored $A$ marks in Section $1$, $B$ marks in section $2$, and $C$ marks in section $3$.

Chef passes the exam if both of the following conditions satisfy:

- Total score of Chef is $\geq 100$;
- Score of each section $\geq 10$.

Determine whether Chef passes the exam or not.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line containing $3$ space-separated numbers $A, B, C$ - Chef's score in each of the sections.
### Output Format

For each test case, output `PASS` if Chef passes the exam, `FAIL` otherwise.

Note that the output is case-insensitive i.e. `PASS`, `Pass`, `pAsS`, and `pass` are all considered same.

### Constraints
- $1 \leq T \leq 1000$
- $0 \leq A, B, C \leq 100$
### Sample 1:
Input
Output

```
5
9 100 100
30 40 50
30 20 40
0 98 8
90 80 80

```

```
FAIL
PASS
FAIL
FAIL
PASS

```

### Explanation:

 **Test Case $1$:**  Although Chef's total score is $209 \geq 100$, still Chef fails the exam since his score in section $1$ is $\lt 10$.

 **Test Case $2$:**  Chef cleared each section's cutoff as well his total score $= 120 \geq 100$.

 **Test Case $3$:**  Although Chef cleared each section's cutoff but his total score is $90 \lt 100$. So he fails the exam.

 **Test Case $4$:**  Although Chef's total score is $106 \geq 100$, still Chef fails the exam since his score in section $1$ is $\lt 10$.

 **Test Case $5$:**  Chef cleared each section's cutoff as well his total score $= 250 \geq 100$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-23T08:54:20.223Z  

```py
t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    h=a+b+c
    if h>=100 and a>=10 and b>=10 and c>=10:
        print("PASS")
    else:
        print("FAIL")
```

---

[View on CodeChef](https://www.codechef.com/problems/PASSTHEEXAM)