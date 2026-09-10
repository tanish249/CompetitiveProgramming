t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    h=a+b+c
    if h%2==0:
        print("YES")
    else:
        print('NO')