import math 

class Solution:
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        h=math.lcm(a,b)
        g=math.gcd(a,b)
        return h,g
        
        