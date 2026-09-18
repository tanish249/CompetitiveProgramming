a,b,c=map(int,input().split())
h=c-a
g=h//b
if g%2==0:
    print("Lucky Chef")
else:
    print("Unlucky Chef")