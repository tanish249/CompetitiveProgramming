class Solution:
    def isSorted(self, arr):
        nums=arr[:]
        nums.sort()
        if arr==nums:
            return True
        else:
            return False
        
    