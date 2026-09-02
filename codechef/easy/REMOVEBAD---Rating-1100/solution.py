t=int(input())
for _ in range(t):
    a=int(input())
    nums=list(map(int,input().split()))
    h=max(nums,key=nums.count)
    g=nums.count(h)
    p=len(nums)
    print(abs(g-p))