import math

t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    h=abs(a-b)
    print(math.ceil(h/c))