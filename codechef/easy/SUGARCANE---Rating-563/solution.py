t=int(input())
for _ in range(t):
    a=int(input())
    p=a*50
    h=int(p*(20/100))
    g=int(p*(30/100))
    f=int(p*(20/100))
    o=h+g+f
    print(abs(p-o))