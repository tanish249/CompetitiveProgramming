a,b,c=map(int,input().split())
h=b*c
if a>h:
    print(abs(a-h))
else:
    print(-1)