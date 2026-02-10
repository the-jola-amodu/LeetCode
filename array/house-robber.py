class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        max_steal = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            max_steal.append(max(max_steal[-1], (max_steal[-2] + nums[i])))
        return max_steal[-1]

        