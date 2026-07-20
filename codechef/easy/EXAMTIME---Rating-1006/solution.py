T = int(input())
for _ in range(T):
    a, b, c = map(int, input().split())
    x, y, z = map(int, input().split())

    h = a + c + b
    g = z + x + y

    if h > g:
        print("DRAGON")
    elif g > h:
        print("SLOTH")
    elif h == g and a > x:
        print("DRAGON")
    elif h == g and x > a:
        print("SLOTH")
    elif h == g and b > y:
        print("DRAGON")
    elif h == g and y > b:
        print("SLOTH")
    else:
        print("TIE")