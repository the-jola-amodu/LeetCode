import math

class Solution(object):
    def reverse(self, x):
        if x < 0:
            x = abs(x)
            ans = 0 - int(str(x)[::-1])
        else:
            ans = int(str(x)[::-1])
        if ans < math.pow(2, 31) and ans > math.pow(-2, 31):
            return ans
        return 0
