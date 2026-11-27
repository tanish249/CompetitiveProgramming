t=int(input())
for _ in range(t):
    nums=list(map(str,input().split()))
    a,b=map(str,input().split())
    if nums[0]==a:
        print(a)
    elif nums[1]==b:
        print(b)