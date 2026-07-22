t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    h=b*c
    if h>=a:
        print("YES")
    else:
        print("no")