class Solution(object):
    def sortedSquares(self, nums):
        resorted = []
        l = 0
        r = len(nums) - 1
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                resorted.append(nums[l] ** 2)
                l += 1
            elif abs(nums[r]) >= abs(nums[l]):
                resorted.append(nums[r] ** 2)
                r -= 1
        resorted = resorted[::-1]
        return resorted
