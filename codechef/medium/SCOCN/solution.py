a=int(input())
nums=list(map(int,input().split()))
b=int(input())
o=nums.count(b)
if o==1 and b in nums:
    print(-2)
elif b in nums:
    print(len(nums) - 1 - nums[::-1].index(b))
else:
    print(-1)
    
    
    
