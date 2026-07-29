t=int(input())
for _ in range(t):
    a,b,c,d,e,f=list(map(int,input().split()))
    num1=[a,b,c]
    num1.sort()
    h=num1[1]+num1[2]
    num2=[f,d,e]
    num2.sort()
    g=num2[1]+num2[2]
    if h>g:
        print('ALICE')
    elif g>h:
        print("BOB")
    else:
        print("TIE")