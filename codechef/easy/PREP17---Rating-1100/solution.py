t=int(input())
for _ in range(t):
    a=int(input())
    num1=list(map(int,input().split()))
    num2=list(map(int,input().split()))
    h=num1+num2
    o=len(h)
    p=len(set(h))
    print(abs(o-p))