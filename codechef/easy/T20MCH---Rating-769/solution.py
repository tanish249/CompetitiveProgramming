a,b,c=map(int,input().split())
h=20-b
g=h*6*6
f=g+c
if f>a:
    print("YES")
else:
    print("NO")