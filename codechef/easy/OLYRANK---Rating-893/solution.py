t=int(input())
for _ in range(t):
    a,b,c,d,e,f=map(int,input().split())
    h=a+b+c
    g=e+f+d
    if h>g:
        print(1)
    else:
        print(2)