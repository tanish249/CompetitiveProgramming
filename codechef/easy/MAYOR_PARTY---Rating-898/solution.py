t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    h=a+c
    if h>b:
        print(h)
    else:
        print(b)