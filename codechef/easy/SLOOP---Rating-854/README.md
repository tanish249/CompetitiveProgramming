# SLOOP - Rating 854

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Coldplay

Chef is a big fan of Coldplay. Every Sunday, he will drive to a park taking $M$ minutes to reach there, and during the ride he will play a single song on a loop. Today, he has got the latest song which is in total $S$ minutes long. He is interested to know how many times will he be able to play the song completely.

### Input Format
- The first line contains an integer $T$ - the number of test cases. Then the test cases follow.
- The only line of each test case contains two space-separated integers $M, S$ - the duration of the trip and the duration of the song, both in minutes.
### Output Format

For each test case, output in a single line the answer to the problem.

### Constraints
- $1 \leq T \leq 1000$
- $1 \leq M \leq 100$
- $1 \leq S \leq 10$
### Subtasks

 **Subtask #1 (100 points):**  original constraints

### Sample 1:
Input
Output

```
3
10 5
10 6
9 10
```

```
2
1
0
```

### Explanation:
- Test case 1: Chef listens to the song once from $0 - 5$ minutes and next from $5 - 10$ minutes.
- Test case 2: Chef listens to the song from $0 - 6$ minutes but now he has only $4$ minutes left so he can't complete the song again.
- Test case 3: Since the song lasts longer than the journey, Chef won't be able to complete it even once.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-07-30T10:33:30.937Z  

```py
t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    print(a//b)
```

---

[View on CodeChef](https://www.codechef.com/problems/SLOOP)