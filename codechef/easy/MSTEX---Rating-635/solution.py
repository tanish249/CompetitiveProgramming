t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    nums=list(map(int,input().split()))
    nums.sort()
    num1=nums[-b:]
    print(sum(num1))
