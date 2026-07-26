t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=7-a
    g=7-b
    if h>g:
        print(g)
    else:
        print(h)