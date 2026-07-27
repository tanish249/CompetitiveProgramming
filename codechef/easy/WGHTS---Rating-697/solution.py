t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    if a==b or a==c or a==d:
        print("YES")
    elif a==b+c or a==b+d or a==c+d:
        print("YES")
    else:
        print("NO")