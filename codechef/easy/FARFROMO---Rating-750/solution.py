t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    h=(a**2+c**2)*0.5
    g=(b**2+d**2)*0.5
    if h>g:
        print("ALEX")
    elif g>h:
        print("BOB")
    else:
        print("EQUAL")