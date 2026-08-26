t=int(input())
for _ in range(t):
    nums=list(map(int,input().split()))
    high = 0 
    low =  0 
    for x in nums:
        if x>=60:
            high +=1
        if x>=30:
            low +=1
    if high>=2 and  low>=4:
        print("Pass")
    else:
        print("Fail")