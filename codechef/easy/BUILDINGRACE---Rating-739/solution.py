t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    h=a/c
    g=b/d
    if h>g:
        print("CHEFINA")
    elif g>h:
        print("chef")
    else:
        print("both")