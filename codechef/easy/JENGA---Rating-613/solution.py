t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    if a==b:
        print("YES")
    elif b>a and b%a==0 :
        print("YES")
    else:
        print("NO")