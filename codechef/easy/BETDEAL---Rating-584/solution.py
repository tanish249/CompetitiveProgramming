t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=abs(100-a)
    g=int(200*(b/100))
    p=abs(200-g)
    if h==p:
        print('BOTH')
    elif p>h:
        print("FIRST")
    elif h>p:
        print("SECOND")