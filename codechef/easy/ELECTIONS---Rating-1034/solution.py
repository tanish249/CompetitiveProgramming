t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    if a>b and a>c and a>50:
        print("A")
    elif b>a and b>c and b>50:
        print("B")
    elif c>a and c>b and c>50:
        print("C")
    else:
        print("NOTA")