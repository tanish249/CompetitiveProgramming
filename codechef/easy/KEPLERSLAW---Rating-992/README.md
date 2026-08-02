# KEPLERSLAW - Rating 992

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Keplers Law

Kepler’s Law states that the planets move around the sun in elliptical orbits with the sun at one focus. Kepler's 3rd law is The Law of Periods, according to which:

- The square of the time period of the planet is directly proportional to the cube of the semimajor axis of its orbit.

You are given the Time periods ($T_1, T_2$) and Semimajor Axes ($R_1, R_2$) of two planets orbiting the same star.

Please determine if the Law of Periods is satisfied or not, i.e, if the constant of proportionality of both planets is the same.

Print `"Yes"` (without quotes) if the law is satisfied, else print `"No"`.

### Input Format
- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- Each test case consists a single line of input, containing four space-separated integers $T_1, T_2, R_1, R_2$.
### Output Format

For each test case, output a single line containing one string — `"Yes"` or `"No"` (without quotes); the answer to the problem.

You may print each character of the answer in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

### Constraints
- $1 \leq T \leq 10^4$
- $1 \leq T_1,T_2 \leq 10$
- $1 \leq R_1,R_2 \leq 10$
### Subtasks

 **Subtask 1(100 points):**  Original constraints

### Sample 1:
Input
Output

```
3
1 1 1 1
1 2 3 4
1 8 2 8
```

```
Yes
No
Yes
```

### Explanation:
- Test Case $1$: $1^2/1^3 = 1^2/1^3$
- Test Case $2$: $1^2/3^3 \neq 2^2/4^3$
- Test Case $3$: $1^2/2^3 = 8^2/8^3$

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-02T10:12:34.240Z  

```py
# cook your dish here
t=int(input())
for i in range(t):
    a=list(map(int,input().split()))
    p=a[0]
    q=a[1]
    r=a[2]
    s=a[3]
    x=(p*p)/(r*r*r)
    y=(q*q)/(s*s*s)
    if x == y:
        print("Yes")
    else:
        print("No")
```

---

[View on CodeChef](https://www.codechef.com/problems/KEPLERSLAW)