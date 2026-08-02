t=int(input())
for _ in range(t):
    a,b,c,d,e=map(int,input().split())
    h=a+b+c+e+d
    if h==0:
        print("Beginner")
    elif h==1:
        print("junior developer")
    elif h==2:
        print("middle developer")
    elif h==3:
        print("senior developer")
    elif h==4:
        print("hacker")
    elif h==5:
        print("Jeff Dean")