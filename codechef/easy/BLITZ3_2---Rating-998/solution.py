t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    h=2*(180+a)
    g=b+c
    print(abs(h-g))