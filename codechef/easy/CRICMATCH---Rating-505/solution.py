t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=b*6
    g=6*h
    if g>=a:
        print("YES")
    else:
        print("NO")