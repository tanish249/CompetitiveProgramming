t=int(input())
for _ in range(t):
    a,b,c,d,e,f=map(int,input().split())
    if (c==a or c==b) and (d==a or d==b):
        print("1")
    elif (e==a or e==b) and (f==a and f==b):
        print("2")
    else:
        print("0")
        
        