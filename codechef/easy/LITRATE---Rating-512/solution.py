t = int(input())
for _ in range(t):
    a, b= map(int, input().split())
    h = b/a
    k = h*100
    if (k>=75):
        print("YES")
    else:
        print("NO")