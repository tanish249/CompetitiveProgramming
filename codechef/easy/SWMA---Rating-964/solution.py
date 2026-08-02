t=int(input())
for _ in range(t):
    a,b=input().split()
    h=str(a)[::-1]
    g=str(b)[::-1]
    if h>b or a>g or a>b or h>g:
        print('YES')
    else:
        print("NO")