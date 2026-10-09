t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    if (  a%b==0 or b%a==0 )and b>=a:
        print("YES")
    else:
        print("NO")