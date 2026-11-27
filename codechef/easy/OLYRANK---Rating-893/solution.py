t=int(input())
for _ in range(t):
    nums=list(map(int,input().split()))
    num1=nums[:3]
    num2=nums[3:]
    h=sum(num1)
    g=sum(num2)
    if h>g:
        print(1)
    else:
        print(2)