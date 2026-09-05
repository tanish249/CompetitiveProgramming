t=int(input())
for _ in range(t):
    a=input()
    h=a.count("1")
    g=a.count("0")
    if h>g:
        print("WIN")
    else:
        print("LOSE")
