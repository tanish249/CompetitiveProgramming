class Solution:
    def isPowerofTwo(self, n):
        h=(bin(n)[2:])
        g=sum(map(int,h))
        if g==1:
            return True
        else:
            return False
            
            
          