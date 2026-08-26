t=int(input())
for _ in range(t):
    a,b,c,d,e,f,g=map(int,input().split())
    if e>=a and f>=b and g>=c and e+f+g>=d:
        print('YES')
    else:
        print("NO")