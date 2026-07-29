t = int(input())

for _ in range(t):
    count = 0
    a, b, c = map(int, input().split())

    h = a * b

    while h < c:
        if a > b:
            b += 1
        else:
            a += 1

        h = a * b
        count += 1

    print(count)