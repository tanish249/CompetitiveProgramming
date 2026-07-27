t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=a+b
    g=abs(21-h)
    if 1<=g<=10:
        print(g)
    else:
        print(-1)