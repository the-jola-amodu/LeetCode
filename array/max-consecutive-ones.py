class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        length = 0
        for n in nums:
            if n:
                length += 1
            else:
                max_ones = max(max_ones, length)
                length = 0
        max_ones = max(max_ones, length)
        return max_ones
        