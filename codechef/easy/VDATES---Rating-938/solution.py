t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    if b<=a<=c:
        print("Take second dose now")
    elif b>a and c>a:
        print("Too Early")
    else:
        print("Too Late")