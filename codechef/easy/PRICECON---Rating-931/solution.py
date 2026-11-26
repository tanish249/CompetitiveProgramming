t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    nums=list(map(int,input().split()))
    h=sum(nums)
    ans=[]
    count =0
    for i in range(len(nums)):
        if b>=nums[i]:
            ans.append(nums[i])
        else:
            count +=1
    g=sum(ans)+count*b
    print(abs(h-g))
   