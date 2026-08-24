t=int(input())
for _ in range(t):
    a=int(input())
    nums=list(map(int,input().split()))
    h=sum(nums)
    if h==0:
        print(0)
    elif h>1:
        print(h//2)
    else:
        print(-1)