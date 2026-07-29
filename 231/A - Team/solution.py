n=int(input())
count = 0
 
for _ in range(n):
    a,b,c=map(int,input().split())
    h=a+b+c
    if h>=2:
        count+=1
print(count)