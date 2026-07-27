t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=a*15
    g=2*b
    if h>=g:
        print("YES")
    else:
        print("NO")
    