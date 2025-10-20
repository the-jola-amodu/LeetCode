class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        left = 0
        current = set()
        for right in range(len(s)):
            if s[right] not in current:
                current.add(s[right])
            else:
                while s[right] in current:
                    current.remove(s[left])
                    left += 1
                current.add(s[right])
            max_length = max(max_length, len(current))
        return max_length