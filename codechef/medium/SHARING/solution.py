a,b=map(int,input().split())
h=a+b
g=a-b
if h%2==0:
    print(int(g/2))
else:
    print(-1)