t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    h=abs(a-b)
    if a==b:
        print('YES')
    elif b>a and c>=h:
        print('YES')
    elif a>b and d>=h:
        print('YES')
    else:
        print('NO')