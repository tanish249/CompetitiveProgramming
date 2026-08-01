t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    h=a/b
    g=c/d
    if h>g:
        print("Alice")
    elif g>h:
        print("BOB")
    else:
        print("EQUAL")