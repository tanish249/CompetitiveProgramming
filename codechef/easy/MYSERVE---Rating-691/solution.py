t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=a+b
    if h%4==0 :
        print('ALICE')
    else:
        print('BOB')