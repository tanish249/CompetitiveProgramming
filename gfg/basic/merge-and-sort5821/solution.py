class Solution:
    def mergeNsort(self, arr1, arr2):
        nums =list(set(arr1 + arr2))

        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2

        left = self.mergeNsort(nums[:mid], [])
        right = self.mergeNsort(nums[mid:], [])

        result = []

        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        while i < len(left):
            result.append(left[i])
            i += 1

        while j < len(right):
            result.append(right[j])
            j += 1

        return result