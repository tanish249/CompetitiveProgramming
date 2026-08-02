t=int(input())
for _ in range(t):
    nums=list(map(int,input().split()))
    nums.sort()
    if nums[1]>=50 and nums[2]>=50:
        print('YES')
    else:
        print("NO")