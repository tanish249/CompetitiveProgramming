t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    if a>c and b>c:
        print("alice")
    elif a>b and c>b:
        print("BOB")
    else:
        print("draw")