class Solution(object):
    def threeSum(self, nums):
        triplets = []
        nums.sort()
        for i in range(len(nums)):
            target = nums[i]
            if target > 0:
                break
            elif i > 0 and target == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                three_sum = target + nums[left] + nums[right]
                if three_sum == 0:
                    triplets.append([target, nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif three_sum > 0:
                    right -= 1
                else:
                    left += 1
        return triplets
        