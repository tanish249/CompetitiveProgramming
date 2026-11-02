t=int(input())
for _ in range(t):
    a=int(input())
    nums=list(map(int,input().split()))
    nums.sort()
    n=len(nums)
    h=nums[n//2]
    count1=0
    count2=0
    for i in range(n):
        if nums[i]>h:
            count1 +=1
        elif h>=nums[i]:
            count2 +=1
    if count2>count1:
        print(count2)
    else:
        print(count1)