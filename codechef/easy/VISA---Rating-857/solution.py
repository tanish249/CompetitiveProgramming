t=int(input())
for _ in range(t):
    a,b,c,d,e,f=map(int,input().split())
    if b>=a and d>=c and e>=f:
        print("yes")
    else:
        print('NO')