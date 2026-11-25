t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    h=a/b
    g=c/d
    if h==g:
        print("Equal")
    elif h>g:
        print("Alice")
    else:
        print("Bob")