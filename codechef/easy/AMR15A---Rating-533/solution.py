a=int(input())
nums=list(map(int,input().split()))
n=len(nums)
count1 = 0 
count2 = 0
for i in range(0,n):
    if nums[i]%2==0:
        count1 +=1
    else:
        count2 +=1
if count1>count2:
    print("READY FOR BATTLE")
else:
    print("NOT READY")