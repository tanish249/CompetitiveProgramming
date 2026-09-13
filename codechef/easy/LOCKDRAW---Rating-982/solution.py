t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    h=a+b
    g=a+c
    f=b+c
    if h==c or g==b or f==a:
        print("YES")
    else:
        print("NO")