# CODETOWN - Rating 1022

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Reach Codetown

Chef embarks on a journey starting from a town named $S$, containing a string of $8$  **uppercase**  English alphabets. His objective is to reach the destination known as `CODETOWN`.

If Chef is currently in town $T_1$, then, with each move, Chef can transition to another town named $T_2$, provided that  **either** :

- $T_2$ is derived from $T_1$ by replacing a consonant with another consonant, or;
- $T_2$ is derived from $T_1$ by replacing a vowel with another vowel.

Find whether Chef can reach `CODETOWN` in any number of moves.
Note that in the english alphabet, letters `A`, `E`, `I`, `O`, and `U` are considered as vowels and rest are considered as consonants.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a string $S$, of length $8$ consisting of uppercase english alphabets.
### Output Format

For each test case, output on a new line, `YES`, if Chef can reach `CODETOWN`, and `NO` otherwise.

You may print each character of the string in uppercase or lowercase (for example, the strings `YES`, `yEs`, `yes`, and `yeS` will all be treated as identical).

### Constraints
- $1 \leq T \leq 10^4$
- $|S| = 8$
- $S$ consists of uppercase english alphabets.
### Sample 1:
Input
Output

```
3
YAPETOWN
CODECHEF
CODETOWN

```

```
YES
NO
YES

```

### Explanation:

 **Test case $1$:**  Chef can reach to `CODETOWN` in the following way: `YAPETOWN` $\rightarrow$ `CAPETOWN` $\rightarrow$ `COPETOWN` $\rightarrow$ `CODETOWN`.

 **Test case $2$:**  It can be shown that Chef would not be able to reach `CODETOWN`.

 **Test case $3$:**  Chef is already in `CODETOWN`.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-23T15:21:29.003Z  

```py
t=int(input())
for _ in range(t):
    a=input()
    if "TOWN" in a:
        print("YES")
    else:
        print("NO")
```

---

[View on CodeChef](https://www.codechef.com/problems/CODETOWN)