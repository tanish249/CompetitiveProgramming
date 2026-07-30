# CREDITS - Rating 809

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Complete the credits

In Uttu's college, a semester is said to be a:

- Overload semester if the number of credits taken $\gt 65$.
- Underload semester if the number of credits taken $\lt 35$.
- Normal semester otherwise

Given the number of credits $X$ taken by Uttu, determine whether the semester is `Overload`, `Underload` or `Normal`.

### Input Format
- The first line will contain $T$ - the number of test cases. Then the test cases follow.
- The first and only of each test case contains a single integer $X$ - the number of credits taken by Uttu.

You may print each character of `Overload`, `Underload` and `Normal` in uppercase or lowercase (for example, `ovErLoAd`, `oVERlOAD`, `OVERLOAD` will be considered identical).

### Output Format

For each test case, output `Overload`, `Underload` or `Normal` depending upon the number of credits taken by Uttu.

### Constraints
- $1 \leq T \leq 100$
- $1 \leq X \leq 100$
### Sample 1:
Input
Output

```
4
65
80
23
58

```

```
Normal
Overload
Underload
Normal

```

### Explanation:

 **Test case-1:**  The semester has $65$ credits. So it is neither an `Overload` semester nor an `Underload` semester. So it is a `Normal` semester.

 **Test case-2:**  The semester has $80$ credits ($\gt 65$). So it is an `Overload` semester.

 **Test case-3:**  The semester has $23$ credits ($\lt 35$). So it is an `Underload` semester.

 **Test case-4:**  The semester has $58$ credits. So it is neither an `Overload` semester nor an `Underload` semester. So it is a `Normal` semester.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-30T13:11:49.611Z  

```py
t=int(input())
for _ in range(t):
    a=int(input())
    if a>65:
        print('OVERLOAD')
    elif 35>a:
        print('Underload')
    else:
        print('Normal')
```

---

[View on CodeChef](https://www.codechef.com/problems/CREDITS)