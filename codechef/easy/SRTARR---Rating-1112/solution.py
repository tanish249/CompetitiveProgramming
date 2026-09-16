t=int(input())
for _ in range(t):
    x=int(input())
    a=input()
    h=a.count("1")
    g=int(a[-1])
    print(abs(h-g))