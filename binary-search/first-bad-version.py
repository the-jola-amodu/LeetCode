# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        left = 0
        right = n
        while left < right:
            middle = (left + right) // 2
            if isBadVersion(middle) == False:
                left = middle + 1
            else:
                right = middle
        return left
        