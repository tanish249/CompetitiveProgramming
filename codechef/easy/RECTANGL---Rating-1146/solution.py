t=int(input())
for _ in range(t):
    nums=list(map(int,input().split()))
    nums.sort()
    if nums[3]==nums[2] and nums[0]==nums[1]:
        print('YES')
    else:
        print("NO")