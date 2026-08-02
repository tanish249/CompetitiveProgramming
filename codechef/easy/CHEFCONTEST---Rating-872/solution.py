t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    h=a+c*10
    g=b+d*10
    if g>h:
        print("CHEF")
    elif h>g:
        print("CHEFINA")
    else:
        print("DRAW")
