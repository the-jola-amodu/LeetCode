class Solution(object):
    def isPerfectSquare(self, num):
        left = 0
        right = num
        while left <= right:
            middle = (left + right) // 2
            if middle * middle == num:
                return True
            elif num > middle * middle:
                left = middle + 1
            else:
                right = middle - 1
        return False
        