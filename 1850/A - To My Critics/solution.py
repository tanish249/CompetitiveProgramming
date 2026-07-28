t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    h=a+b 
    g=b+c 
    l=a+c
    if(h>=10 or g>=10 or l>=10):
        print("YES")
    else:
        print("NO")