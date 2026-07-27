import math 

t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=abs(a-b)
    print(math.ceil(h/8))