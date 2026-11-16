t=int(input())
for _ in range(t):
    num1=input()
    num2=input()
    ans=[]
    for i in range(len(num1)):
        if num1[i]==num2[i]:
            ans.append("G")
        else:
            ans.append("B")
    print("".join(ans))