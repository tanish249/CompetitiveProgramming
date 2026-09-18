t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=abs(a)
    g=abs(b)
    p=h+g
    if p%2==0:
        print("YES")
    else:
        print("NO")