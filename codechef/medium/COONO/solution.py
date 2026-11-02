t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    h=a+b
    if h==c:
        print("YES")
    else:
        print("NO")