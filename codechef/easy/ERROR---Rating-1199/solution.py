t=int(input())
for _ in range(t):
    a=input()
    if "010" in a or "101" in a:
        print("GOOD")
    else:
        print("BAD")