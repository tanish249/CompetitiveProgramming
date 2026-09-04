a,b=map(int,input().split())
num1=list(map(int,input().split()))
num2=list(map(int,input().split()))
nums=num1+num2
nums.sort()
print(*nums)