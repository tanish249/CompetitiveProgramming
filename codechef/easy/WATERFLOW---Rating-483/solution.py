t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    h=a+c*d
    if h==b:
        print("Filled")
    elif h>b:
        print("OVERFLOW")
    else:
        print("Unfilled")