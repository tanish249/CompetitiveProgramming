class Solution:
    def binarySearch(self, arr, k):
        left = 0
        right = len(arr) - 1
        while left <=right:
            mid = (left + right ) // 2
            if k ==arr[mid]:
                return True
            elif k > arr[mid]:
                left = mid + 1
            elif k < arr[mid]:
                right = mid - 1
        else:
            return False
            
            
    
         