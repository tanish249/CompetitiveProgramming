t=int(input())
for _ in range(t):
    a=input()
    h=int(a[0]+a[1])
    g=int(a[3]+a[4])
    if h>=12 and 12>=g:
        print("DD/MM/YYYY")
    elif 1<=g<=12 and 1<=h<=12:
        print("BOTH")
    else :
        print("MM/DD/YYYY")