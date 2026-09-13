class Solution:
    def isDigitSumPalindrome(self, n):
        h=list(map(int,str(n)))
        g=sum(h)
        f=str(g)
        d=int(f[::-1])
        if d==g or g==d:
            return True
        else:
            return False