import math
t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    h=c//30
    g=a+h
    f=math.ceil(g/b)
    print(f)