t=int(input())
for _ in range(t):
    a=int(input())
    h=a//5
    if a%5==0:
        print(abs(a-h))
    else:
        print(a)