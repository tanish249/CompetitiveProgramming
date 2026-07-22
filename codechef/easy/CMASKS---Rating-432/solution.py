t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=a*100
    g=b*10
    if h==g or h>g:
        print("Cloth")
    else:
        print("Disposable")