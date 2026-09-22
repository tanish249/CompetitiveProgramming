class Solution:
    def isPalindrome(self, s):
        h=s[::-1]
        if h==s:
            return True
        else:
            return False