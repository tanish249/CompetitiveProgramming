arr = tuple(map(int, input().split()))
h=len(arr)
o=len(set(arr))
if h==o:
    print("True")
else:
    print("False")