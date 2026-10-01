t=int(input())
for _ in range(t):
    a=int(input())
    nums=list(map(int,input().split()))
    n=len(nums)
    count = 0 
    for i in range(0,n):
        if nums[i]>=1000:
            count +=1
    print(count)