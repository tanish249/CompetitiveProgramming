t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=a//3
    g=abs(a-h)
    print(g*b)