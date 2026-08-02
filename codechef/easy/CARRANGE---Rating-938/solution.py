t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    h=abs(a-1)
    g=abs(h-b)
    print(g*c)