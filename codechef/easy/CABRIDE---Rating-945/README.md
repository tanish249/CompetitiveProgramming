# CABRIDE - Rating 945

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Cab Rides

Chef and his family is trying to reach the airport. Including Chef, they are a total of $N$ members.

A single cab ride costs $\max(200, 100 \cdot X)$ rupees to transport $X$ people from Chef's home to the airport. Further, a cab can fit  **at most 4 people**.

Chef may have to book multiple cabs in order for his entire family to reach the airport. What is the minimum cost for Chef's family to reach the airport if they take cabs optimally?

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case contains a single integer $N$ - the number of people in Chef's family.
### Output Format

For each test case, output on a new line the minimum cost.

### Constraints
- $1 \le T \le 50$
- $1 \le N \le 50$
### Sample 1:
Input
Output

```
4
1
4
5
6

```

```
200
400
500
600

```

### Explanation:

 **Test Case 1**  : Chef takes a cab alone, which costs him $200$.

 **Test Case 2**  : All $4$ members can fit in a single cab, costing $\max(200, 100 \cdot 4) = 400$.

 **Test Case 3**  : $3$ members take a single cab costing $300$, and then the last $2$ members take another cab costing $200$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-26T12:42:43.195Z  

```py
t=int(input())
for _ in range(t):
    a=int(input())
    h=100*a
    print(max(200,h))
```

---

[View on CodeChef](https://www.codechef.com/problems/CABRIDE)