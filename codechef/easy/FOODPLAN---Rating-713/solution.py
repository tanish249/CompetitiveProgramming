t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=a*(10/100)
    g=abs(a-h)
    if b>g:
        print("ONLINE")
    elif b==g:
        print('EITHER')
    else:
        print("DINING")