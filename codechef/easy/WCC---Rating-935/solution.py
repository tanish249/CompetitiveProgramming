t=int(input())
for _ in range(t):
    a=int(input())
    q=input()
    h=q.count("C")
    g=q.count("D")
    j=q.count("N")
    if h==j:
        print(55*a)
    elif h>j:
        print(60*a)
    else:
        print(40*a)