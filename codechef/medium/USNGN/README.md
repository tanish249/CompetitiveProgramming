# USNGN

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Username Generator

You are given a user's $S$ name and birth year $Y$.

The username is formed by converting the entire name to  **lowercase**  and appending the  **last two digits of the birth year**.

If the last two digits contain a leading zero, it must be preserved. For example, the year `2001` contributes `01`.

Generate and print the username.

### Input Format

The first line contains the string $S$ — the user's name.

The second line contains an integer $Y$ — the birth year.

### Output Format

Print the generated username.

### Constraints
- $1 \le |S| \le 100$
- $S$ consists only of uppercase and lowercase English letters.
- $1900 \le Y \le 2025$
### Sample 1:
Input
Output

```
Alice
1995
```

```
alice95
```

### Explanation:

The lowercase form of `Alice` is `alice`, and the last two digits of `1995` are `95`.

Therefore, the username is `alice95`.

### Sample 2:
Input
Output

```
Bob
2001
```

```
bob01
```

### Explanation:

The lowercase form of `Bob` is `bob`, and the last two digits of `2001` are `01`.

Therefore, the username is `bob01`.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-02T08:39:38.129Z  

```py
a=input().lower()
b=input()
h=b[-2]+b[-1]
print(a+h)
```

---

[View on CodeChef](https://www.codechef.com/problems/USNGN)