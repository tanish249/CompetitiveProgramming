t=int(input())
for _ in range(t):
    a=input()
    h=int(a[0]+a[1])
    g=int(a[3]+a[4])
    if 1<=g<=12 and 1<=h<=12:
        print("BOTH")
    elif 1<=h<=12:
        print("MM/DD/YYYY")
    else:
        print("DD/MM/YYYY")
 