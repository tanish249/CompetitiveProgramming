t=int(input())
for _ in range(t):
    a,b,c,d,e=map(int,input().split())
    h=e*c
    g=e*d
    o=a+h
    p=b+g
    if o==p:
        print("SAME PRICE")
    elif o>p:
        print('DIESEL')
    else:
        print("PETROL")