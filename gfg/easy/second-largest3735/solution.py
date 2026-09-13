class Solution:
    def getSecondLargest(self, arr):
        h=sorted(set(arr))
        g=len(h)
        if g==1:
            return -1
        else:
            return h[-2]