a,b,c=map(int,input().split())
h=a//2
f=min(h,b)
g=min(h,c)
if a>b and a>c:
    print(min(f,g))
else:
    print(f+g)