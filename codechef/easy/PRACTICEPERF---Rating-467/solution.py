nums=list(map(int,input().split()))
n=len(nums)
count = 0 
for i in range(0,n):
    if nums[i]>=10:
        count +=1
print(count)