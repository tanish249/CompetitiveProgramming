t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    even=a//2
    odd=(a+1)//2
    print(even*b+odd*c)