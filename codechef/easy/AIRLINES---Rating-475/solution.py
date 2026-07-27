t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    h=10*a
    if h>=b:
        print(b*c)
    elif b>h:
        print(h*c)