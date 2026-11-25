t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    h=a+b
    g=h/2
    if g>c:
        print("YES")
    else:
        print("NO")