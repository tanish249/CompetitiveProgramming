t=int(input())
for _ in range(t):
    a=int(input())
    nums=list(map(int,input().split()))
    h=sum(nums)
    if h%2!=0:
        print("Yes")
    else:
        print("No")