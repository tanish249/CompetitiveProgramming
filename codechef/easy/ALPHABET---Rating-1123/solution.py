a=input()
t=int(input())
for _ in range(t):
    b=input()
    h=sorted(set(a))
    g=sorted(set(b))
    if h==g:
        print("Yes")
    else:
        print("No")