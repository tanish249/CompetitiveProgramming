t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    nums=list(map(int,input().split()))
    nums.sort()
    print(sum(nums[-b:]))