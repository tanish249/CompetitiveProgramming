class Solution:
    def findUnion(self, a, b):
        h = a + b
        g = sorted(set(h))
        return g