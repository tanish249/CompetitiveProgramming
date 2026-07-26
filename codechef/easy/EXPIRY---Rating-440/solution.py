t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    h=b*c
    if(a==h):
        print("YES")
    elif(h>a):
        print("YES")
    elif(a>h):
        print("NO")