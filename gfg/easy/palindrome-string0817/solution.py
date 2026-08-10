class Solution:
    def isPalindrome(self, a):
        h=a[::-1]
        if h==a:
            return True
        else:
            return False