class Solution(object):
    def longestConsecutive(self, nums):
        nums = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in nums:
                length = 1
                while (num + length) in nums:
                    length += 1
                longest = max(length, longest)
        return longest
        