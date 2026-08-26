t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    h=b+(100-a)*c
    print(h*10)