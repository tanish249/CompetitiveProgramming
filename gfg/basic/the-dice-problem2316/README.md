# Opposite Side of Dice

![Difficulty](https://img.shields.io/badge/Difficulty-Basic-red)

## Problem

You are given a  **cubic dice**  with  **6**  faces. All the individual faces have a number printed on them. The numbers are in the range of  **1 to 6**, like any ordinary dice. Given the face of this cube, find the number on the opposite side of the cube.

 **Examples:** 

```
Input: n = 6
Output: 1
Explanation: For dice facing number 6 opposite face will have the number 1.
```

```
Input: n = 2
Output: 5
Explanation: For dice facing number 5 opposite face will have the number 2.
```

 **Constraints:** 
1 <= n <= 6

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-16T09:02:11.221Z  

```py
class Solution:
    def oppositeFaceOfDice(self, n):
    	h=7-n
    	return h
    	
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/the-dice-problem2316/1)