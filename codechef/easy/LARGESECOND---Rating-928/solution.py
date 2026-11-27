t=int(input())
for _ in range(t):
    a=int(input())
    nums=list(map(int,input().split()))
    h=list(set(nums))
    h.sort()
    print(h[-1]+h[-2])
   