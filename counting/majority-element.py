class Solution(object):
    def majorityElement(self, nums):
        mode = 0
        occurence = 0
        num_dict = {}
        for num in nums:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        for key, value in num_dict.items():
            if value > occurence:
                mode = key
                occurence = value
        return mode
        