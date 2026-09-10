t=int(input())
for _ in range(t):
    a=int(input())
    nums=list(map(int,input().split()))
    nums.sort()
    h=sum(nums)
    g=nums[0]
    print(h+g*-1)