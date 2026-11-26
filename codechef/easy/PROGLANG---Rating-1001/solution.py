t=int(input())
for _ in range(t):
    a,b,c,d,e,f=map(int,input().split())
    num1=[c,d]
    num2=[e,f]
    if a in num1 and b in num1:
        print(1)
    elif a in num2 and b in num2:
        print(2)
    else:
        print(0)