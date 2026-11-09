# update the code below to solve this problem

import math

t = int(input())
for i in range(t):
    a,b=map(int,input().split())
    h=math.gcd(a,b)
    print(h)