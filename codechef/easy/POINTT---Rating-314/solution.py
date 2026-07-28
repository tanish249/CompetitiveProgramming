a,b,c,d=map(int,input().split())
if a>c:
    print("Alice")
elif c>a:
    print("bob")
elif a==c and b>d:
    print("Alice")
elif a==c and d>b:
    print("bob")
else:
    print("ALICE")