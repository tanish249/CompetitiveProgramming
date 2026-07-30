t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=abs(100-a)
    g=200*b//100
    l=200-g
    if l>h:
        print("first")
    elif h>l:
        print('second')
    else:
        print("both")