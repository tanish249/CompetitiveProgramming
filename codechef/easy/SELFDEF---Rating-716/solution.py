t=int(input())
for _ in range(t):
    a=int(input())
    nums=list(map(int,input().split()))
    n=len(nums)
    count = 0
    for i in range(n):
        if 10<=nums[i]<=60:
            count +=1
    print(count)