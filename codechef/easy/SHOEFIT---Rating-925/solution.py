t=int(input())
for _ in range(t):
    nums=list(map(int,input().split()))
    if 0 in nums and 1 in nums:
        print(1)
    else:
        print(0)