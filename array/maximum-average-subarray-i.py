class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        the_sum = sum(nums[:k])
        max_average = the_sum/k
        for i in range(k, len(nums)):
            the_sum = the_sum - nums[i - k] + nums[i]
            average = the_sum/k
            max_average = max(average, max_average)
        return max_average

        