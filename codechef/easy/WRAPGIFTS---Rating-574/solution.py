t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())

    h = (a * b + b * c + a * c)
    k = 2 * h
    f = 1000 / k

    print(int(f))