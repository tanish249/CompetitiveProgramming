class Solution:
    def intersection(self, arr1, arr2):
        h=set(arr1)
        g=set(arr2)
        common=[]
        
        for i in g:
            if i in h:
                common.append(i)
        common.sort()
        return common
    
