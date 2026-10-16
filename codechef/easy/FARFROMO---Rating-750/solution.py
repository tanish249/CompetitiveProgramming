t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    h=abs(a+c)
    g=abs(b+d)
    if h==g:
        print("EQUAL")
    elif h>g:
        print("ALEX")
    else:
        print("BOB")