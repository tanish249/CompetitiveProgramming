t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=a**4+4*b**2
    g=4*b*a**2
    if h==g:
        print('YES')
    else:
        print('NO')
    