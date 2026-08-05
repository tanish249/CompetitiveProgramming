t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    in1=(a*100)//10
    in2=(b*100)//20
    if in1==in2:
        print('ANY')
    elif in1>in2:
        print("FIRST")
    elif in2>in1:
        print("SECOND")