t=int(input())
for _ in range(t):
    a,b,c,d,e=map(int,input().split())
    h=a//d
    g=a//e
    o=h*b
    p=g*c
    if o==p:
        print("ANY")
    elif p>o:
        print("PETROL")
    else:
        print('DIESEL')