t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=a*2
    if a<b:
        print(abs(a-b))
    elif a>b:
        print(abs(h-b))
    