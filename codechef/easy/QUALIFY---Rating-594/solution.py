t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    h=b+c*2
    if a>=h:
        print("Qualify")
    else:
        print("NotQualify")