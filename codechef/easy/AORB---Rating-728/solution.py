t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    o=a+b
    h=500-a*2
    g=1000-o*4
    l=h+g
    q=1000-b*4
    w=500-o*2
    r=q+w
    if l>r or l==r:
        print(l)
    else:
        print(r)
  