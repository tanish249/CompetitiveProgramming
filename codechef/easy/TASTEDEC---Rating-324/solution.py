t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=a*2
    g=b*5
    if(h>g):
        print("Chocolate")
    elif(h<g):
        print("Candy")
    elif(h==g):
        print("Either")