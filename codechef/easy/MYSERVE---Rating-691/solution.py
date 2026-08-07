t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=(a+b)+1
    if h%3==0:
        print("bob")
    else:
        print("alice")