class Solution:
    def thirdLargest(self,arr):
        nums=arr[:]
        nums.sort()
        h=len(nums)
        if 3>h:
            return -1
        else:
            return nums[-3]