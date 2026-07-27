t=int(input())
for _ in range(t):
    nums=list(map(int,input().split()))
    nums.sort()
    h=nums[1]+nums[2]
    print(h)