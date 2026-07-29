t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=a*b
    g=str(h)
    l=len(g)
    if l==5 and g[0]!=0:
        print("YES")
    else:
        print("NO")
   