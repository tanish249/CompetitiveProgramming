class Solution:
    def countOddEven(self, arr):
        n = len(arr)
        count1 = 0
        count2 = 0

        for i in range(0, n):
            if arr[i] % 2 == 0:
                count1 += 1
            elif arr[i] % 2 != 0:
                count2 += 1

        return count2, count1