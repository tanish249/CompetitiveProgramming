t=int(input())
for _ in range(t):
    x=int(input())
    a=input()
    h=a.count("0")
    g=a.count("1")
    print(max(h,g))