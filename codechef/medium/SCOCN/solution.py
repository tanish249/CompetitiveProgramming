a=int(input())
nums=list(map(int,input().split()))
b=int(input())
o=nums.count(b)
q=nums.index(b)
w=nums.index(b,q+1)
if o==1 and b in nums:
    print(-2)
elif b in nums:
    print(w)
else:
    print(-1)
