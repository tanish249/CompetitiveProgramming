t=int(input())
p=input()
q=p.count("a")
w=p.count("e")
e=p.count("i")
r=p.count("o")
t=p.count("u")
o=max(q,w,e,r,t)
if o==q:
    print('a')
elif o==w:
    print('e')
elif o==e:
    print('i')
elif o==r:
    print("o")
else:
    print("u")