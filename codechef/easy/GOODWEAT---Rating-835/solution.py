t=int(input())
for _ in range(t):
    n=list(map(int,input().split()))
    h=(n.count(1))
    g=(n.count(0))
    if h>g:
        print("YES")
    else:
        print('NO')