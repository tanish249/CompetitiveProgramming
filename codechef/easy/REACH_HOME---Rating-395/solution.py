t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=a*5
    if h>=b:
        print("YES")
    else:
        print("NO")