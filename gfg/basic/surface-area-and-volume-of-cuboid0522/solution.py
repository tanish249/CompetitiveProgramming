class Solution:
    def find(self, l, b, h):
        a=2*(b*h+h*l+l*b)
        b=l*b*h
        arr=[a,b]
        return arr
    
        