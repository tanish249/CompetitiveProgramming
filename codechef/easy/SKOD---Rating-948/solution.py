t=int(input())
for _ in range(t):
    a=int(input())
    nums=list(map(int,input().split()))
    nums.sort()
    h=nums[1:]
    print(sum(h))