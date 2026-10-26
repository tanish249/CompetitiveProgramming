t=int(input())
for _ in range(t):
    a=int(input())
    nums=list(map(int,input().split()))
    h=nums.count(1)
    g=nums.count(-1)
    p=abs(sum(nums))
    o=len(nums)
    if h==g:
        print(0)
    elif o%2!=0:
        print(-1)
    else:
        print(p//2)