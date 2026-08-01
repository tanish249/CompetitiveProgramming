t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    h=5*b
    g=int(a/h)
    print(g+c)