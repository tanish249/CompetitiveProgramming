import math 

a,b=map(int,input().split())
p=a+1
h=p*4+b*3
print(math.ceil(h/8))