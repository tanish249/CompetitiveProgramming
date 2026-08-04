a,b,c=map(int,input().split())
h=a+c
k=h-b
if(b>h):
    print(0)
elif(h==b):
    print(1)
elif(h>b):
    print(k+1)
    