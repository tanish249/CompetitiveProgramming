import math

a=int(input())
nums=list(map(int,input().split()))
n=len(nums)
p=math.ceil(n/2)
if n%2!=0:
    print(nums[p-1])
else:
    print(nums[n//2-1])