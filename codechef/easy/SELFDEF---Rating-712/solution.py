import math

t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=math.ceil(b/100)
    if h>a:
        print(abs(h-a))
    else:
        print(0)
