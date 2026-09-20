# The Else Statement

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Take an interger input  **a**, and then use the if statement to print " **Big** " (without quotes) if the given number is greater than 100, and use the else statement to print " **Small** " (without quotes) when the number is smaller than or equal to 100.

 **Note:**  After printing the output, you should move the cursor to the new line.

 **Examples:** 

```
Input: a = 10
Output: Small
Explanation: 10 is smaller than 100, so our else statement works and we print Small.
```

```
Input: a = 101
Output: Big
Explanation: 101 is greater than 100, so our if statement works and we print Big.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-20T11:07:22.248Z  

```py
a=int(input())
if a>100:
    print("Big")
else:
    print("Small")
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/the-else-statement--115735/1)