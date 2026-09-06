t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    h=abs(a-c)
    g=abs(b-d)
    if h==0 or g==0:
        print("YES")
    else:
        print("NO")