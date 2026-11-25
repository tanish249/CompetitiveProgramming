t=int(input())
for _ in range(t):
    nums=list(map(int,input().split()))
    num1=nums[:3]
    num2=nums[3:]
    num1.sort()
    num2.sort()
    h=sum(num1)-num1[0]
    g=sum(num2)-num2[0]
    if h==g:
        print("Tie")
    elif h>g:
        print("Alice")
    else:
        print("Bob")