t=int(input())
for _ in range(t):
    a,b,c,d,e=map(int,input().split())
    h=a//c
    g=b//d
    p=min(h,g)
    if p>=e:
        print("YES")
    else:
        print("NO")