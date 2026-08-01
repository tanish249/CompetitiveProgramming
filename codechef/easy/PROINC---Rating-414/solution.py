t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=abs(a-b)
    g=int(a*(10/100))
    p=a+g
    print(p-h)