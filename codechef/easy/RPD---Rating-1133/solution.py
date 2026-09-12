t=int(input())
for _ in range(t):
    a=int(input())
    nums=list(map(int,input().split()))
    nums.sort()
    h=nums[-1]
    g=nums[-2]
    f=h*g
    nam=list(map(int,str(f)))
    print(sum(nam))