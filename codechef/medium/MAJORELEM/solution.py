class Solution:
    def majorityElement(self, arr):
        h=max(arr,key=arr.count)
        return h
