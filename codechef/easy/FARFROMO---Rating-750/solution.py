t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    h=abs(a+c)
    g=abs(b+d)
    if h>g:
        print("ALEX")
    elif g>h:
        print("BOB")
    else:
        print("EQUAL")