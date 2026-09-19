import math

class Solution:

    def average(self, a, b):
        h=sum(a)
        g=b.count("out")
        if g==0:
            return -1
        else:
            return math.ceil(h/g)