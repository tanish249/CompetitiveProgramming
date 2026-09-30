import math 
a,b,c=map(int,input().split())
h=math.ceil(a/2)
f=min(h,b)
g=min(h,c)
print(max(f,g))