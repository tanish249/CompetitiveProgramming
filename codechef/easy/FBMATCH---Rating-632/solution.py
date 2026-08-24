t=int(input())
for _ in range(t):
    a=int(input())
    x=input()
    h=max(x, key=x.count)
    p=(x.count(h))
    if p>=2:
        print('YES')
    else:
        print("NO")