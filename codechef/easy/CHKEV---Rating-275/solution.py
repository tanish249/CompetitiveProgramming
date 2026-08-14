# cook your dish here
L, R = map(int, input().split())

if L % 2 == 0 or L != R:
    print("Yes")
else:
    print("No")