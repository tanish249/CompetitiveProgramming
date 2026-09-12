t=int(input())
for _ in range(t):
    a=int(input())
    nums=list(map(int,input().split()))
    
    n=len(nums)
    for i in range(n):
        for j in range(n-1-i):
            if nums[j] > nums[j+1]:
               nums[j] , nums[j+1] = nums[j+1] , nums[j]
    print(nums[1])