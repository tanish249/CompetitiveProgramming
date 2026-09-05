t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    f=min(a,b)
    g=min(b,c)
    h=min(c,a)
    if f==g and g==h and f==g:
        print("YES")
    else:
        print("NO")