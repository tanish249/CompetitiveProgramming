t=int(input())
for _ in range(t):
    a,b,c,d,e,f,g,h,i,j=map(int,input().split())
    num1=[a,c,e,g,i]
    num2=[b,d,f,h,j]
    q=num1.count(1)
    w=num2.count(1)
    if q==w:
        print(0)
    elif q>w:
        print(1)
    else:
        print(2)
   