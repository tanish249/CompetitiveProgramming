a=int(input())
a=input().lower()
distinct=set(a)
if len(distinct)==26:
    print("YES")
else:
    print("NO")