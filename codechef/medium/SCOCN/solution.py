a=int(input())
nums=list(map(int,input().split()))
b=int(input()) 
if b in nums:
    print(nums.index(b))
else:
    print(-1)