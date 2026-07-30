t=int(input())
for _  in range(t):
    a=list(map(str,input().split()))
    h=a[0]+a[1]+a[2]
    g=a[3]+a[4]+a[5]
    j=a[1]+a[2]+a[3]
    k=a[2]+a[3]+a[4]
    if h=="WWW"or g=="WWW" or j=="WWW" or k=="WWW":
        print("YES")
    else:
        print("NO")