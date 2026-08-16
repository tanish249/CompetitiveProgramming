# PRIMEDICE - Rating 643

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Hackerman

Hackerman wants to know who is the better player between Bob and Alice with the help of a game.

The game proceeds as follows:

- First, Alice throws a die and gets the number $A$
- Then, Bob throws a die and gets the number $B$
- Alice wins the game if the sum on the dice is a prime number; and Bob wins otherwise.

Given $A$ and $B$, determine who wins the game.

### Input Format
- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case contains two space-separated integers $A$ and $B$.
### Output Format

For each test case, output on a new line the winner of the game: `Alice` or `Bob`.

Each letter of the output may be printed in either uppercase or lowercase, i.e, `Alice`, `ALICE`, `AlIce` and `aLIcE` will all be considered equivalent.

### Constraints
- $1 \leq T \leq 36$
- $1 \leq A \leq 6$
- $1 \leq B \leq 6$
### Sample 1:
Input
Output

```
3
2 1
1 1
2 2

```

```
Alice
Alice
Bob

```

### Explanation:

 **Test case $1$:**  $A = 2$ and $B = 1$. Their sum is $2+1 = 3$ which is a prime number, so Alice wins.

 **Test case $2$:**  $A = 1$ and $B = 1$. Their sum is $1+1 = 2$ which is a prime number, so Alice wins.

 **Test case $3$:**  $A = 2$ and $B = 2$. Their sum is $2 + 2 = 4$ which is not a prime number, so Bob wins.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-16T08:34:34.504Z  

```py
t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=a+b
    
    if h<2:
        print("BOB")
    else:
        for i in range(2,h):
            if h%i==0:
                print("BOB")
                break
        else:
            print("ALICE")

```

---

[View on CodeChef](https://www.codechef.com/problems/PRIMEDICE)