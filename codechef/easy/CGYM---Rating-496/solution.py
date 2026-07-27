t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    if c>=a+b:
        print(2)
    elif c>=a:
        print(1)
    else:
        print(0)