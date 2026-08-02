t=int(input())
for _ in range(t):
    a,b=input().split()
    h=str(a)[::-1]
    g=str(b)[::-1]
    if h>g or a>b:
        print('YES')
    else:
        print("NO")