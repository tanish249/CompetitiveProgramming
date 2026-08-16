t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=a+b
    
    if h<2:
        print("BOB")
    else:
        for i in range(2,h):
            if h%i==0:
                print("BOB")
                break
        else:
            print("ALICE")
