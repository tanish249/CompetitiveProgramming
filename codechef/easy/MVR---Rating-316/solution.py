a,b,c,d=map(int,input().split())
h=a*2+b
g=c*2+d
if h==g:
    print("EQUAL")
elif h>g:
    print("Messi")
elif g>h:
    print("Ronaldo")