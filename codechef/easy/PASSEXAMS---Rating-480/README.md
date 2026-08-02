# PASSEXAMS - Rating 480

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Passing Exams

Chef gave a series of $3$ exams, and scored $X$, $Y$ and $Z$ in them respectively, out of $100$ marks each.

Chef needs to get $50$ or more marks in at least $2$ out of $3$ exams to pass. Determine if Chef passed.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first line contains $3$ integers - $X$, $Y$ and $Z$.
### Output Format

For each test case, output on a new line $\text{Yes}$ or $\text{No}$ depending on whether Chef passed or not.

### Constraints
- $1 \le T \le 100$
- $0 \le X, Y, Z \le 100$
### Sample 1:
Input
Output

```
4
50 50 0
15 100 100
40 40 100
0 0 0

```

```
Yes
Yes
No
No
```

### Explanation:

 **Test Case 1:**  Chef scored $50$ or more marks in the first and second exams, therefore he passed.

 **Test Case 3**  : Chef scored $50$ or more in only the third exam. Therefore, he did not pass.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-02T07:06:26.938Z  

```py
t=int(input())
for _ in range(t):
    nums=list(map(int,input().split()))
    nums.sort()
    if nums[1]>=50 and nums[2]>=50:
        print('YES')
    else:
        print("NO")
```

---

[View on CodeChef](https://www.codechef.com/problems/PASSEXAMS)