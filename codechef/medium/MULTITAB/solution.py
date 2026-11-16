t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=a*3
    if b>=h:
        print("YES")
    else:
        print("NO")