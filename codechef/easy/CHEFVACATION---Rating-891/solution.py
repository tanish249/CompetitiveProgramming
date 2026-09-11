t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    if c>a+b and (c>a or c>b):
        print("YES")
    else:
        print("NO")