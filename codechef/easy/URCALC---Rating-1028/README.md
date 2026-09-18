# URCALC - Rating 1028

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Program Your Own CALCULATOR

Write a program to obtain 2 numbers $($ $A$ $and$ $B$ $)$ and an arithmetic operator $(C)$ and then design a $calculator$ depending upon the operator entered by the user.

So for example if C="+", you have to sum the two numbers.

If C="-", you have to subtract the two numbers.

If C=" * ", you have to print the product.

If C=" / ", you have to divide the two numbers.

###Input:

- First line will contain the first number $A$.
- Second line will contain the second number $B$.
- Third line will contain the operator $C$, that is to be performed on A and B.

###Output: Output a single line containing the answer, obtained by, performing the operator on the numbers. Your output will be considered to be correct if the difference between your output and the actual answer is not more than $10^{-6}$.

###Constraints

- $-1000 \leq A \leq 1000$
- $-1000 \leq B \leq 1000$ $and$ $B \neq 0$
- $C$ $can$ $only$ $be$ $one$ $of$ $these$ $4$ $operators$ {" + ", " - ", " * ", " / "}
### Sample 1:
Input
Output

```
8
2
/

```

```
4.0

```

### Sample 2:
Input
Output

```
5
3
+

```

```
8

```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-18T06:28:46.370Z  

```py
a=int(input())
b=int(input())
c=input()
if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
else:
    print(a/b)
```

---

[View on CodeChef](https://www.codechef.com/problems/URCALC)