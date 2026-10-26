t=int(input())
for _ in range(t):
    a=int(input())
    h=list(map(int,str(a)))
    g=sum(h)
    if g%10==0:
        print("Valid")
    else:
        print("Invalid")