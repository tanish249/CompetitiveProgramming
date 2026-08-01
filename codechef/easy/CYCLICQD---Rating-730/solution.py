t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())

    h = b * 3
    g = a - b
    j = g * -1
    p = h + j

    if p >= c:
        print("PASS")
    else:
        print("FAIL")