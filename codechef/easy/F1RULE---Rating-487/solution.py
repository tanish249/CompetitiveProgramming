t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    h=a*(107/100)
    if b>h:
        print("NO")
    else:
        print('YES')
  