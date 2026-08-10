# LB03A - Rating 580

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Problem 3 (High Accuracy) - Read the problem

There are $100$ questions in a paper.

- Each question carries +3 marks for correct answer,
- -1 marks for incorrect answer i.e. one mark is deducted for each incorrect answer,
- 0 marks for an unattempted question.

It is given that Chef received exactly $X$ $(0 \leq X \leq 100)$ marks.
Determine the  **minimum**  number of problems Chef marked  **incorrect**.

### Sample 1:
Input
Output

```
4
0
100
32
18

```

```
0
2
1
0

```

### Explanation:

 **Test Case $1$:**  It might be possible that Chef didn't attempt any question in which case he didn't get any question incorrect.

 **Test Case $2$:**  In the case where the Chef answered $34$ questions correctly, they would have got $102$ marks ($34$ * $3$), and if they answered $2$ questions incorrectly, their marks would have been reduced by $2$, resulting in a total of $100$ marks. So, the minimum number of problems Chef marked incorrect in this case is $2$.

 **Test Case $3$:**  In the case where the Chef answered $11$ questions correctly, they would have got $33$ marks ($11$ * $3$), and if they answered $1$ questions incorrectly, their marks would have been reduced by $1$, resulting in a total of $32$ marks. So, the minimum number of problems Chef marked incorrect in this case is $1$.

 **Test Case $4$:**  For the case when Chef got $6$ questions correct, they would have got $18$ marks ($6$ * $3$) and he didn't get any question incorrect.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-10T08:13:31.548Z  

```py
# Update the program below to solve the problem

t = int(input())            
for i in range(t):          
    a,b,c= map(int, input().split())
    if c%a==0 and c%b==0:
        print("ANY")
    elif c%a==0:
        print("CHICKEN")
    elif c%b==0:
        print("DUCK")
    else:
        print("NONE")
```

---

[View on CodeChef](https://www.codechef.com/problems/LB03A)