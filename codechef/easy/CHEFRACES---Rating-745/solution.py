t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    num1=[a,b]
    num2=[c,d]
    count = 0 
    for i in num2:
        if i in num1:
            count +=1
    if count==0:
        print(2)
    elif count==1:
        print(1)
    else:
        print(0)