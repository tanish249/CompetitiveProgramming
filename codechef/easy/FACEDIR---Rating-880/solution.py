t=int(input())
for _ in range(t):
    a=int(input())
    if a%4==0:
        print("North")
    elif a%4==2:
        print("South")
    elif a%4==1:
        print('East')
    else:
        print("West")