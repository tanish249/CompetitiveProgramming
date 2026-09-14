# Switch Statement

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given a number  **n**, use a switch statement to return "One" if the given number is equal to 1, "Two" if the number is 2 and so on till 9 ("Nine") else return "Unknown"(without quotes). 

 **Examples:** 

```
Input: n = 10
Output: Unknown
```

```
Input: n = 1
Output: One
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-14T04:50:41.447Z  

```py
a=int(input())
if a==1:
    print("One")
elif a==2:
    print("Two")
elif a==3:
    print("Three")
elif a==4:
    print("Four")
elif a==5:
    print("Five")
elif a==6:
    print("Six")
elif a==7:
    print("Seven")
elif a==8:
    print("Eight")
elif a==9:
    print("Nine")
else:
    print("Unknown")
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/switch-statement/1)