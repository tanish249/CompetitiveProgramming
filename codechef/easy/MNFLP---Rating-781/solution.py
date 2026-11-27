t=int(input())
for _ in range(t):
    a=int(input())
    nums=list(map(int,input().split()))
    h=nums.count(1)
    g=nums.count(-1)
    p=abs(h-g)
    if sum(nums)==0:
        print(0)
    elif p%2==0:
        print(p//2)
    else:
        print(-1)