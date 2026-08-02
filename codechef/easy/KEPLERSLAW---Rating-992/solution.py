# cook your dish here
t=int(input())
for i in range(t):
    a=list(map(int,input().split()))
    p=a[0]
    q=a[1]
    r=a[2]
    s=a[3]
    x=(p*p)/(r*r*r)
    y=(q*q)/(s*s*s)
    if x == y:
        print("Yes")
    else:
        print("No")