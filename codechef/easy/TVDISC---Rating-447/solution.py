t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    h=a-c
    g=b-d
    if g>h:
        print("First")
    elif h>g:
        print("Second")
    elif h==g:
        print("Any")