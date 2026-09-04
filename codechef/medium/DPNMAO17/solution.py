import math

a,b,c=map(int,input().split())
nums=list(map(int,input().split()))
h=sum(nums)
g=a*b
if h>g:
    print(math.ceil(h/g))
else:
    print(0)