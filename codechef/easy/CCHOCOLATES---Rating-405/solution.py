t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    h=a*5+b*10
    print(h//c)