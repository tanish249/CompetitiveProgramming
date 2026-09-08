# BSEX01

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Search in a 2D Matrix

You are given an  **N × M**  matrix where:

- Each row is sorted in ascending order.
- The first integer of each row is greater than the last integer of the previous row.

Your task is to find if an integer  **Target**  exists in the matrix.

 **Note:**  You must implement a solution with a time complexity faster than  **O(N + M)**.

### Input Format
- The first line contains two integers, N and M, separated by a space, representing the number of rows and columns in the matrix, respectively.
- The next N lines each contain M integers, representing the elements of the matrix.
- The final line contains a single integer, Target, which is the value to search for in the matrix.
### Output Format
- Print YES if the Target exists in the matrix.
- Print NO otherwise.
### Constraints
- $1 \leq m, n \leq 100$
- $-10^4 \leq \text{matrix}[i][j], \text{target} \leq 10^4$
- The matrix is guaranteed to be non-empty and sorted.
### Sample 1:
Input
Output

```
3 4
1 3 5 7 
10 11 16 20 
23 30 34 60
3

```

```
YES
```

### Explanation:
- Test case 1: The target 3 exists in the matrix
### Sample 2:
Input
Output

```
3 4
1 3 5 7 
10 11 16 20 
23 30 34 60
13
```

```
NO
```

### Explanation:
- Test case 2: The target 13 does not exists in the matrix

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-08T13:59:53.402Z  

```py
a,b=map(int,input().split())
num1=list(map(int,input().split()))
num2=list(map(int,input().split()))
num3=list(map(int,input().split()))
p=int(input())
if p in num1 or p in num2 or p in num3:
    print("YES")
else:
    print("NO")
```

---

[View on CodeChef](https://www.codechef.com/problems/BSEX01)