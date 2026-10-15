t=int(input())
for _ in range(t):
    a=int(input())
    nums=list(map(int,input().split()))
    h=max(nums)
    g=min(nums)
    print(h-g)