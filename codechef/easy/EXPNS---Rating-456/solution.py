t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=30*b
    if a>=h:
        print("YES")
    else:
        print("NO")