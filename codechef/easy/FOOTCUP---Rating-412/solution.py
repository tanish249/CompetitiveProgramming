t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=a+b
    if a==b and h>0 :
        print("YES")
    else:
        print("NO")