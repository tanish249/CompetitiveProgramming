t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=a+b
    if h<3:
        print(1)
    elif 3<=h<=10:
        print(2)
    elif 11<=h<=60:
        print(3)
    elif h>60:
        print(4)