t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    h=a+c
    g=b+d
    if h==180 or g==180:
        print("YES")
    else:
        print("NO")