import math
t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=abs(b-a)
    g=math.ceil(h/8)
    print(g)