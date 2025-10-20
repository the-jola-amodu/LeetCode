class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        lor = [f'{nums[0]}']
        for i in range(1, len(nums)):
            if nums[i] - 1 == nums[i-1] and '>' not in lor[-1]:
                lor[-1] += f'->{nums[i]}'
            elif nums[i] - 1 == nums[i-1] and '>' in lor[-1]:
                lor[-1]= lor[-1][:-len(str(nums[i-1]))] + str(nums[i])
            elif nums[i] - 1 != nums[i-1]:
                lor.append(f'{nums[i]}')
        return lor

        