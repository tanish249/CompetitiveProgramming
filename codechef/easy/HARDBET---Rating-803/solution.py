t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    if b>a and c>a:
        print("Draw")
    elif a>b and c>b:
        print("Bob")
    else:
        print("Alice")