class Solution:
    def findMedian(self, arr):
        arr.sort()
        n=len(arr)
        h=sum(arr)
        o=arr[n//2-1]
        p=arr[n//2]
        if n%2!=0:
            return p
        else:
            return (o+p)/2
            
    
