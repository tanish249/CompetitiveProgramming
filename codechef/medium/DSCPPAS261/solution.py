class Solution:
    def intersect(self, nums1, nums2):
        common = []
        for i in nums1:
            if i in nums2:
                common.append(i)
        return common