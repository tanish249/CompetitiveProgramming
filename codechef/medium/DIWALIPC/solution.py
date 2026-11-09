t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    h=a+b*c
    if d>=h:
        print("YES")
    else:
        print("NO")