# cook your dish here
T = int(input())
for i in range(T):
    N,M=map(int,input().split())
    h=abs(N-M)
    if h%2==0:
        print("YES")
    else:
        print("NO")