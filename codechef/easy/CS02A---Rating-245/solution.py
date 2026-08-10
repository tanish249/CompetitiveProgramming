# Update the program below to solve the problem

t = int(input())           
for i in range(t):
    X, Y, A = map(int, input().split())
    if A>=X and Y>A:
        print("YES")
    else:
        print("NO")
