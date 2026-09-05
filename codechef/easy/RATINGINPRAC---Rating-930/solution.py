t=int(input())
for _ in range(t):
    a=int(input())
    nums=list(map(int,input().split()))
    h=list(nums)
    h.sort()
    if h==nums:
        print("YES")
    else:
        print("NO")

  