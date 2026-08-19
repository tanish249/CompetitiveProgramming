t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=24-a
    g=h*60
    print(g-b)