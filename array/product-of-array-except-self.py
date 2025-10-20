import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        template = nums.copy()
        pre = 1
        post = 1
        nums[0] = 1
        for i in range(1, len(template)):
            pre *= template[i - 1]
            nums[i] = pre
        for i in range(len(template) - 2, -1, -1):
            post *= template[i + 1]
            nums[i] *= post
        return nums
            
        