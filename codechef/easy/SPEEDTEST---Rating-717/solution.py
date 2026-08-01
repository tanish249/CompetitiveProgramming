import math 

t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=math.ceil(a/10)
    g=math.ceil(b/10)
    print(abs(h-g))