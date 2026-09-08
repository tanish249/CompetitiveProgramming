a,b=map(int,input().split())
num1=list(map(int,input().split()))
num2=list(map(int,input().split()))
num3=list(map(int,input().split()))
p=int(input())
if p in num1 or p in num2 or p in num3:
    print("YES")
else:
    print("NO")