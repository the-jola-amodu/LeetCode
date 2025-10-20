class Solution(object):
    def is_fast_enough(self, hour, speed, piles):
        time = 0
        for pile in piles:
            time += math.ceil(pile / speed)
        if time <= hour:
            return True
        return False

    def minEatingSpeed(self, piles, h):
        possible_speeds = max(piles)
        left = 1
        right = possible_speeds
        while left < right:
            middle = (left + right) // 2
            if self.is_fast_enough(h, middle, piles):
                right = middle
            else:
                left = middle + 1
        return left
        