t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    h=abs(a-b)
    g=c*2
    if g>=h:
        print("YES")
    else:
        print("NO")