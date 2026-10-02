t=int(input())
for _ in range(t):
    a,b,c,d,e,f=map(int,input().split())
    x=[a,b]
    num1=[c,d]
    num2=[e,f]
    x.sort()
    num1.sort()
    num2.sort()
    if x==num1:
        print(1)
    elif x==num2:
        print(2)
    else:
        print(0)