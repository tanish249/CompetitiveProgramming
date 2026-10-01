t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    nums=list(map(int,input().split()))
    n=len(nums)
    count = 0
    for i in range(0,n):
        if nums[i]>=b:
            count +=1
    print(count)
            