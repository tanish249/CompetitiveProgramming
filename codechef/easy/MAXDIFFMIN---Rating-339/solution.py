t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    h = max(a, b, c)
    g = min(a, b, c)
    print(h - g)