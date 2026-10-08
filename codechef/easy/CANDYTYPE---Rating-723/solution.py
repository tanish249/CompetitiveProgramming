t=int(input())
for _ in range(t):
    a=int(input())
    nums=list(map(int,input().split()))
    nums.sort()
    h=max(nums,key=nums.count)
    print(h)