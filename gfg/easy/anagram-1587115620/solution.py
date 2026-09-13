class Solution:
    def areAnagrams(self, s1, s2):
        h=sorted(s1)
        g=sorted(s2)
        if h==g:
            return True
        else:
            return False
     
     
       