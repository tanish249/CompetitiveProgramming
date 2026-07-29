t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    h=(b-c)
    g=h*d
    print(a+g)