t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    h=a-c
    k=b-d
    if(h<k):
        print("First")
    elif(h>k):
        print("Second")
    elif(h==k):
        print("Any")