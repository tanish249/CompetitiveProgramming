t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    if a>b:
        print(0)
    else:
        print((abs(a-b))*2)