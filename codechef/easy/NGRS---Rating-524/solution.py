t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h= (a/100)*100
    k= (b/100)*100
    if(h<50):
        print("Z")
    elif(h>=50 and k<50):
        print("F")
    else:
        print("A")