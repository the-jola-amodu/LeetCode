class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_ones = 0
        left = 0
        num_zeros = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                num_zeros += 1
            while num_zeros > k:
                if nums[left] == 0:
                    num_zeros -= 1
                left += 1
            length = right - left + 1
            max_ones = max(max_ones, length)
        return max_ones
        