import math

t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=math.ceil(b/100)
    g=abs(a-h)
    if(h>a):
         print(g)
    else:
        print(0)

        
  