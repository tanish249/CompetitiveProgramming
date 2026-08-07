t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=(a+b)
    if h%4==0 or h%4==1:
        print("alice")
    else:
        print("bob")