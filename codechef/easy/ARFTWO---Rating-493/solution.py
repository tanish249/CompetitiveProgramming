t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    h=a+b
    g=a+c
    p=b+a
    if h>=d or g>=d or p>=d:
        print("YES")
    else:
        print("NO")