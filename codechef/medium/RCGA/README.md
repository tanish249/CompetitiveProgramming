# RCGA

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Round Card Game

Suneet and Slavic each have  **two cards**, with each card having a value between `1` and `10`.

Suneet's cards have values $a_1$ and $a_2$, while Slavic's cards have values $b_1$ and $b_2$.

The game consists of exactly  **two rounds**. In each round, both players reveal one of their remaining cards. The player with the greater card value wins that round. If both cards have the same value, the round is a draw.

After two rounds, Suneet wins the game if he has won  **strictly more rounds**  than Slavic.

Each player can choose either of their two cards for the first round, with the remaining card used in the second round. Therefore, there are exactly  **4 possible ways**  the game can be played. Two cards are treated as separate choices even if they have the same value.

Find the  **number of ways in which Suneet wins the game**.

### Input Format

The first line contains four space-separated integers $a_1$, $a_2$, $b_1$, and $b_2$.

### Output Format

Print a single integer — the number of ways in which Suneet wins the game.

### Constraints
- $1 \le a_1,a_2,b_1,b_2 \le 10$
### Sample 1:
Input
Output

```
3 8 2 6
```

```
2
```

### Explanation:

Among the four possible orders in which the cards can be played, Suneet wins in exactly  **2**  of them.

Therefore, the answer is `2`.

### Sample 2:
Input
Output

```
1 1 1 1
```

```
0
```

### Explanation:

Every round is a draw regardless of the order in which the cards are played.

Therefore, Suneet wins in `0` ways.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-11T10:40:32.410Z  

```py
nums=set(list(map(int,input().split())))
n=len(nums)
if n>1:
    print(int(n/2))
else:
    print(0)
```

---

[View on CodeChef](https://www.codechef.com/problems/RCGA)