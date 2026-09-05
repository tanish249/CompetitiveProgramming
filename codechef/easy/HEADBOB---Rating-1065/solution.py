t=int(input())
for _ in range(t):
    a=int(input())
    b=input()
    if "I" in b:
        print("INDIAN")
    elif "Y" in b and "N" in b:
        print("NOT INDIAN")
    else:
        print("NOT SURE")