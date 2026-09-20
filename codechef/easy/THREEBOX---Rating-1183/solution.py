t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    h=a+c+b
    g=h%d
    if h==d:
        print(1)
    else:
        print(g+1)