t=int(input())
for _ in range(t):
    a=int(input())
    if 3>=a:
        print("BRONZE")
    elif a>3 and 6>=a:
        print("silver")
    elif a>6:
        print("GOLD")