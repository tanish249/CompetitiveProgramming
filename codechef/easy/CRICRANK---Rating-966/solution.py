t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    x,y,z=map(int,input().split())
    if a> x and c>z:
        print("A")
    elif b>y and c>z:
        print("A")
    elif a>x and b>y:
        print("A")
    else:
        print("B")