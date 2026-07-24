a,b,c=map(int,input().split())
h=abs(50-c)
g=h*b
if 50>=c:
    print(a)
elif c>50:
    print(a+g)