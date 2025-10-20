class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setified = set(nums)
        if len(nums) == len(setified):
            return False
        return True