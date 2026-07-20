t=int(input())
for _ in range(t):
    a=int(input())
    if 1<=a<=10:
        print("Lower Double")
    elif 11<=a<=15:
        print("Lower Single")
    elif 16<=a<=25:
        print("Upper Double")
    elif 26<=a<=30:
        print("Upper Single")