t=int(input())
for _ in range(t):
    nums=list(map(int,input().split()))
    h=sum(nums)
    if h%2==0:
        print("NO")
    else:
        print("YES")