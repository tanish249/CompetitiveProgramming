t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    h=a*b
    g=c//2
    print(g//h)