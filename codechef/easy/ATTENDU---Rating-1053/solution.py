t=int(input())
for _ in range(t):
    a=int(input())
    x=input()
    h=x.count("1")
    f=abs(120-a)
    u=h+f
    y=(u/120)*100
    if y>=75.00:
        print('YES')
    else:
        print('NO')
    
    