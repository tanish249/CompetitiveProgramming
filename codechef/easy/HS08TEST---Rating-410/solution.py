a,b=map(float,input().split())
h=b-a

if a%5==0 and b>=a-0.50:
    print(f"{h-0.50:.2f}")
else:
    print(f"{b:.2f}")