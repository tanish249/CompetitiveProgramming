# Update the program below to solve the problem

t = int(input())            
for i in range(t):          
    a,b,c= map(int, input().split())
    if c%a==0 and c%b==0:
        print("ANY")
    elif c%a==0 and c:
        print("CHICKEN")
    else:
        print("NONE")