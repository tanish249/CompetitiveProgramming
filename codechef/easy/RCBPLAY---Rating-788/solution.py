t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    h=a+2*c
    if h>=b:
        print("YES")
    else:
        print("NO")