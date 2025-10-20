class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        distance = 99999999999999
        num = 0
        for i in nums:
            if abs(i) < distance or abs(i) == distance and i > num:
                num = i
                distance = abs(i)
        return num
        