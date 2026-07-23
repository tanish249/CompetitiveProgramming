t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    h=abs(a-b)
    print(h*c)