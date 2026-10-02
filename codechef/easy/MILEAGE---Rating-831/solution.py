t=int(input())
for _ in range(t):
    a,b,c,d,e=map(int,input().split())
    h=a//d
    g=a//e
    if h*b>g*c:
        print("DIESEL")
    elif h*b==g*c:
        print("ANY")
    else:
        print("PETROL")