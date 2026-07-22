t=int(input())
for _ in range(t):
nums=list(map(int,input().split()))
nums.sort()
if nums[0]>=60 and nums[1]>=60:
    print("PASS")
elif nums[0]>=30 and nums[1]>=30 and nums[2]>=30 and nums[3]>=30:
    print("PASS")
else:
    print("FAIL")