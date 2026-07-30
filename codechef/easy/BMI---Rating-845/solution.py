t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    g=b*b
    h=a//g
    if(h<=18):
        print(1)
    elif(h<=24):
        print(2)
    elif(h<=29):
        print(3)
    elif(h>=30):
        print(4)
