# Convert Celsius To Fahrenheit

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

Given a temperature in celsius  **C**. You need to convert the given temperature into  **Fahrenheit**.

 **Examples:** 

```
Input: C = 32
Output: 89.6
Explanation: Using the conversion formula of celsius to farhenheit, it can be calculated that, for 32 degree celsius, the temperature in Fahrenheit = 89.6
```

```
Input: C = 50
Output: 122
Explanation: Using the conversion formula of celsius to farhenheit, it can be calculated that, for 50 degree C, the temperature in Fahrenheit = 122.
```

 **Constraints:** 
1 ≤ C ≤ 104

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-16T08:59:46.757Z  

```py
class Solution:
    def cToF(self,C):
        h=(C*9/5)+32
        return h 

```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/convert-celsius-to-fahrenheit/1)