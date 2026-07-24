# INDDAY - Rating 173

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Independence Day

India's independency day is on the $15^{th}$ of August. You are given a date $X$ August, and must find how many days are left for the independence day.

If the independence day has passed already, print $-1$ instead.

### Input Format
- The first and only line of input contains a single integer $X$ - the date in August.
### Output Format

Output the number of days left for independence day or $-1$ if it has already passed.

### Constraints
- $1 \le X \le 31$
### Sample 1:
Input
Output

```
1

```

```
14

```

### Explanation:

There are still $14$ days left for Independence day.

### Sample 2:
Input
Output

```
15

```

```
0

```

### Explanation:

$15^{th}$ August is the Independence day itself, hence the answer is $0$.

### Sample 3:
Input
Output

```
17

```

```
-1

```

### Explanation:

Independence day has already passed.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-24T14:11:15.297Z  

```py
a=int(input())
if 15>=a:
    print(abs(15-a))
else:
    print(-1)
```

---

[View on CodeChef](https://www.codechef.com/problems/INDDAY)