import math 

a,b=map(int,input().split())
h=math.ceil(a/10)
g=h*10
if g+a>=100:
    print("YES")
else:
    print("NO")