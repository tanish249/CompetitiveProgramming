t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=a/b
    if(h%2==0):
        print("YES")
    else:
        print("NO")