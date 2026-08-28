t=int(input())
for _ in range(t):
    a=input()
    b=input()
    h=list(sorted(a))
    g=list(sorted(b))
    if h==g:
        print("YES")
    else:
        print("NO")
    