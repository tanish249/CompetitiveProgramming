t=int(input())
for _ in range(t):
    x=int(input())
    nums=list(map(int,input().split()))
    h=sum(nums)
    p=len(nums)
    g=h/p
    if g>=4.0 and 2 not in nums and 5 in nums:
        print("Yes")
    else:
        print("No")
