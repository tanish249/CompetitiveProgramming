t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    h=a*b
    g=a+c
    print(min(h,g))