t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    h=a+b+c
    if a>b>c or a<b<c or (a%2==0 and b%2==0 and c%2==0):
        print('YES')
    else:
        print('NO')