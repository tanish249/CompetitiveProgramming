t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    h=a-b
    g=c-d
    p=h+g
    if 0>p:
        print("yes")
    else:
        print("No")