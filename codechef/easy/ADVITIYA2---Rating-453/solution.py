t=int(input())
for _ in range(t):
    a,b,c,d,e=map(int,input().split())
    h=a+b+c+d+e
    if h>=4:
        print("YES")
    else:
        print("NO")