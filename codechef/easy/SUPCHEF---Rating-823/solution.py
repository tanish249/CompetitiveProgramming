t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    h=c*b
    if(a>h):
        print("YES")
    else:
        print("NO")
