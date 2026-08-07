t=int(input())
for _ in range(t):
   a,b,c=map(int,input().split())
   h=a+b
   g=b+c
   p=a+c
   print(max(h,g,p))