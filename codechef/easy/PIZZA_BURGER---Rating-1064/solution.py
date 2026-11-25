t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    if a>b:
        print("PIZZA")
    elif a>c:
        print("BURGER")
    else:
        print("NOTHING")