a = int(input())
b = int(input())

area = a * b
peri = 2 * (a + b)

if peri > area:
    print("peri")
    print(peri)
elif area > peri:
    print("area")
    print(area)
else:
    print("Eq")
    print(area)