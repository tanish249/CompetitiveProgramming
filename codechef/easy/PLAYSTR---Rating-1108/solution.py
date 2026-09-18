t=int(input())
for _ in range(t):
    x=int(input())
    a=input()
    b=input()
    h=a.count("0")
    g=a.count("1")
    o=b.count("0")
    p=b.count("1")
    if h==o and g==p:
        print("YES")
    else:
        print("NO")