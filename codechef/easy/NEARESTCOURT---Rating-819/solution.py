import math

t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=abs(a-b)
    g=math.ceil(h/2)
    print(g)