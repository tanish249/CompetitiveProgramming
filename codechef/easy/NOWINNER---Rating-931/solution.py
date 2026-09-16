t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    h=a+b+c
    if h%2==0 and d%2==0:
        print("NO")
    else:
        print("YES")