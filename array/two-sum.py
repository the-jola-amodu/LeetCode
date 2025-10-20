class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_map:
                return [i, num_map[complement]]
            num_map[nums[i]] = i
        return []
        