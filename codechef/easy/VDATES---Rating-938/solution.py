t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    if b<=a<=c:
        print("Take second dose now")
    elif a>c:
        print("Too Late")
    elif b>a:
        print("Too Early")