import math

t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=abs(a-b)
    if a>b:
        print(math.ceil(h/4))
    else:
        print(0)