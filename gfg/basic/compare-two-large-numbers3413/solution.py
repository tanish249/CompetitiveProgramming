class Solution:
    def check(self, a, b):
        a=int(a)
        b=int(b)
        if a<b:
            return 1
        elif a>b:
            return 2
        elif a==b:
            return 3