t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=b*3
    if a>=h:
        print(a//h)
    else:
        print(0)