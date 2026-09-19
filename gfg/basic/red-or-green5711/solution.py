class Solution:
    def redOrGreen(self, s: str) -> int:
        h=s.count("G")
        g=s.count("R")
        if h>g:
            return g
        else:
            return h