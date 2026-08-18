t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=100/a
    g=225/b
    if h>g:
        print("small")
    elif h==g:
        print("equal")
    else:
        print("large")