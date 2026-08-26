# PSGRADE - Rating 904

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Passing Marks

Recently, Chef's College Examination has concluded. He was enrolled in $3$ courses and he scored $A, B, C$ in them, respectively. To pass the semester, he must score at least $A_{min}, B_{min}, C_{min}$ marks in the respective subjects along with a cumulative score of at least $T_{min}$, i.e, $A + B + C \ge T_{min}$.

Given seven integers $A_{min}, B_{min}, C_{min}, T_{min}, A, B, C$, tell whether Chef passes the semester or not.

###Input:

- The first line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of a single line of input, seven integers $A_{min}, B_{min}, C_{min}, T_{min}, A, B, C$ each separated by aspace.

###Output: Output in a single line, the answer, which should be "YES" if Chef passes the semester and "NO" if not.

You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

###Constraints

- $1 \leq T \leq 100$
- $1 \leq A_{min}, B_{min}, C_{min}, A, B, C \leq 100$
- $A_{min} + B_{min} + C_{min} \leq T_{min} \leq 300$
### Sample 1:
Input
Output

```
5
1 1 1 300 2 2 2
3 2 2 6 2 2 2
2 3 2 6 2 2 2
2 2 3 6 2 2 2
100 100 100 300 100 100 100
```

```
NO
NO
NO
NO
YES
```

### Explanation:

 **TestCase 1:**  Chef is passing in all the subjects individually but his total score ($2 + 2 + 2 = 6$) is much below the required threshold of $300$ marks. So Chef doesn't pass the semester.

 **TestCase 2:**  Chef's score in the first subject is less than the threshold, so he doesn't pass the semester.

 **TestCase 3:**  Chef's score in the second subject is less than the threshold, so he doesn't pass the semester.

 **TestCase 4:**  Chef's score in the third subject is less than the threshold, so he doesn't pass the semester.

 **TestCase 5:**  Chef is passing in all the subjects individually and also his total score is equal to the required threshold of $300$ marks. So Chef passes the semester.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-26T05:50:20.576Z  

```py
t=int(input())
for _ in range(t):
    a,b,c,d,e,f,g=map(int,input().split())
    if e>=a and f>=b and g>=c and e+f+g>=d:
        print('YES')
    else:
        print("NO")
```

---

[View on CodeChef](https://www.codechef.com/problems/PSGRADE)