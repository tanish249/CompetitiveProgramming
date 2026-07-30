t=int(input())
for _ in range(t):
    a,b,c,d,e=map(int,input().split())
    h=a-b
    g=c+d+e
    if h>=g:
        print("YES")
    else:
        print("NO")