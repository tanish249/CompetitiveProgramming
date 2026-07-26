t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    h=abs(b-c)
    print(a*h)