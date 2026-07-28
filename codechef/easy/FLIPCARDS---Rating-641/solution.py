t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=abs(a-b)
    print(min(h,b))