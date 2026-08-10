class Solution:
    def check_odd_pairs(self, A, B, C):
        h = A + B
        g = B + C
        f = A + C

        if h % 2 != 0 or g % 2 != 0 or f % 2 != 0:
            return "YES"
        else:
            return "NO"