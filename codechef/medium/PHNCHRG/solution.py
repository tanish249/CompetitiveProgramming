t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    h=abs(80-a)
    g=h*b
    f=20*c
    p=100-a
    if a>=80:
        print(p*c)
    else:
        print(g+f)