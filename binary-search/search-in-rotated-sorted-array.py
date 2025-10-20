class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left < right:
            middle = (left + right) // 2
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle

        min_index = right
        if target == nums[min_index]:
            return min_index
        elif target >= nums[0] and target <= nums[max(min_index - 1, 0)]:
            left = 0
            right = min_index - 1
        else:
            left = min_index + 1
            right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif target > nums[middle]:
                left = middle + 1
            else:
                right = middle - 1
        return -1
                
        