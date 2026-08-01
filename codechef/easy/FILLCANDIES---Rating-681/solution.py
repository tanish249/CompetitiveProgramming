import math

t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    h=b*c
    print(math.ceil(a/h))