t = int(input())

for _ in range(t):
    a = int(input())
    nums = list(set(map(int, input().split())))

    nums.sort()

    h = nums[-1]
    g = nums[-2]

    print(h + g)