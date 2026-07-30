t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    h=c//a
    g=d//b
    print(h+g)