t=int(input())
for _ in range(t):
    a=int(input())
    x=input()
    y=input()
    d=x.count("0")
    f=x.count("1")
    g=y.count("0")
    h=y.count("1")
    if d==g and f==h:
        print("YES")
    else:
        print("NO")