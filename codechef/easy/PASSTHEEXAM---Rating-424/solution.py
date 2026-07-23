t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    h=a+b+c
    if h>=100 and a>=10 and b>=10 and c>=10:
        print("PASS")
    else:
        print("FAIL")