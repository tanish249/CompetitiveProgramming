t=int(input())
for _ in range(t):
    n=int(input())
    h=list(map(int,str(n)))
    if sum(h)%10==0:
        print("Valid")
    else:
        print("Invalid")