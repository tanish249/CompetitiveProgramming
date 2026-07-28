a,b=map(int,input().split())
if b>a:
    print("UNLOCKED")
else:
    print(abs(a-b))