t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    if (a==d or b==d):
        print("TIE")
    elif(b<d):
        print("P")
    elif(b>d):
        print("Q")