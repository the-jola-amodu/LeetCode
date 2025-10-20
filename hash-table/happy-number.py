class Solution(object):
    def isHappy(self, n):
        seen = set()
        while n not in seen:
            seen.add(n)
            sum_ = 0
            for letter in str(n):
                sum_ += int(letter) * int(letter)
            n = sum_
            if n == 1:
                return True
        return False
        