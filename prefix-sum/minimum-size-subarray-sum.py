class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        left = 0
        summation = 0
        for right in range(len(nums)):
            summation += nums[right]
            while summation >= target:
                min_length = min(min_length, right - left + 1)
                summation -= nums[left]
                left += 1
        return 0 if min_length == float('inf') else min_length
        