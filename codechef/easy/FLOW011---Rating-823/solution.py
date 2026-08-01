t=int(input())
for _ in range(t):
    a=int(input())
    h=a*(10/100)
    g=a*(90/100)
    p=a*(98/100)
    if 1500>a:
        print(a+g+h)
    elif a>=1500:
        print(a+500+p)