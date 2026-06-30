t = int(input())
ans = 0

for _ in range(t):
    a, b = map(int, input().split())
    if b - a >= 2:
        ans += 1

print(ans)