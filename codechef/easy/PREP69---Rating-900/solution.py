t=int(input())
for _ in range(t):
    a=int(input())
    nums=list(map(int,input().split()))
    h=sorted(set(nums))
    print(len(h))
    print(*h)