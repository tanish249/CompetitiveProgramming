t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=abs(a-b)
    if a==b:
        print(0)
    else:
        print(b//a)