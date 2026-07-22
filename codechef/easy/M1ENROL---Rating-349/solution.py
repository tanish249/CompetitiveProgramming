t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    if b>a:
        print(abs(a-b))
    else:
        print(0)