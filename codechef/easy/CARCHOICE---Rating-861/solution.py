t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    h=c//a
    g=d//b
    if g>h:
        print(-1)
    elif h==g:
        print(0)
    else:
        print(1)