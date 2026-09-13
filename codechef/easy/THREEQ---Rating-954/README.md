# THREEQ - Rating 954

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### The Old Saint And Three Questions

Once upon a time, there was a hero and an old saint. And like in any story with a hero and an old saint, the old saint asked the hero — three questions!

But here's the twist: each question was a  **binary**  question, which means that the answer to each must be either a 'Yes' or a 'No', not none, not both. Our hero, who was not so wise in the ways of science, answered them arbitrarily and just hoped he is correct. The old saint, being so old, does not remember which answers were correct. The only thing that he remembers is - how many of them were 'Yes', and how many of them were 'No'. Our hero will pass the test if the old saint cannot distinguish his responses from the  **set**  of correct answers i.e. if the number of 'Yes' and 'No' in the responses matches that in the correct answers, regardless of their order.

You are given the answers to each of the three questions, and the responses of the hero to the same. Find whether the hero will be able to pass the old saint's test.

### Input Format
- First line will contain $T$, the number of test cases. The description of the test cases follow.
- The first line of each test case consists of three space-separated integers $A_1$ $A_2$ $A_3$, representing the correct answers to the first, second, and third question respectively ($0$ for 'No', $1$ for 'Yes').
- The second line of each test case consists of three space-separated integers $B_1$ $B_2$ $B_3$, representing the response of the hero to the first, second, and third question respectively ($0$ for 'No', $1$ for 'Yes').
### Output Format

For each test case, print "Pass" (without quotes) if the hero passes the old saint's test, "Fail" (without quotes) otherwise.

### Constraints
- $1 \leq T \leq 64$
- $0 \leq A_i, B_i \leq 1$
### Sample 1:
Input
Output

```
2
1 0 1
1 1 0
0 0 0
1 1 1
```

```
Pass
Fail
```

### Explanation:
- In the first test case, since the number of $1s$ (Yes) is $2$, and the number of $0s$ (No) is $1$ among both the correct answers and the hero's answers, the old saint will fail to distinguish. Hence, the hero passes the test.
- In the second test case, the number of $1s$ (Yes) is $0$ among the correct answers but $3$ among the hero's responses. Similarly, the number of $0s$ don't match. Therefore, the old saint will be able to call the differences between the correct answer and the hero's response. Hence, the hero fails the test.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-13T05:44:59.311Z  

```py
t=int(input())
for _ in range(t):
    num1=list(map(int,input().split()))
    num2=list(map(int,input().split()))
    g=num1.count(0)
    h=num1.count(1)
    x=num2.count(0)
    y=num2.count(1)
    if g==x and h==y:
        print("PASS")
    else:
        print("FAIL")
```

---

[View on CodeChef](https://www.codechef.com/problems/THREEQ)