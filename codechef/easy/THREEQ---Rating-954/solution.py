t=int(input())
for _ in range(t):
    num1=list(map(int,input().split()))
    num2=list(map(int,input().split()))
    g=num1.count(0)
    h=num1.count(1)
    x=num2.count(0)
    y=num2.count(1)
    if g==x and h==y:
        print("Pass")
    else:
        print("Fail")