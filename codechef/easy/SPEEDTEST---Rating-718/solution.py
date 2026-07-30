t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    h=a/b
    g=c/d 
    if h>g:
        print("alice")
    elif g>h:
        print("bob")
    else:
        print("equal")