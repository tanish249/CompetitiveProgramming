a,b=map(float,input().split())
h=b-a
g=a-0.50

if a%5==0 and b>=g:
    print(f"{h-0.50:.2f}")
else:
    print(f"{b:.2f}")