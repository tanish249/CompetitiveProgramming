t=int(input())
for _ in range(t):
    a=int(input())
    if a<=100:
        print(a)
    elif 100<a<=1000:
        print(abs(a-25))
    elif 1000<a<=5000:
        print(abs(a-100))
    elif a>5000:
        print(abs(a-500))