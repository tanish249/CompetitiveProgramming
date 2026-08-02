t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    g = a * b
    h = 10 * g / 100

    if a > 1000:
        print(f"{g - h:.6f}")
    else:
        print(f"{g:.6f}")