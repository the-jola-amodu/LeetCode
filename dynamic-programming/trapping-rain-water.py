class Solution(object):
    def trap(self, height):
        water = 0
        left = 0
        right = 0
        max_left = [0] * len(height)
        max_right = [0] * len(height)
        for i in range(len(height)):
            j = -i -1
            max_left[i] = left
            max_right[j] = right
            left = max(left, height[i])
            right = max(right, height[j])
        for i in range(len(height)):
            water += max(0, min(max_right[i], max_left[i]) - height[i])
        return water


        