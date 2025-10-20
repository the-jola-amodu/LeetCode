from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        storage = defaultdict(int)
        window = defaultdict(int)
        min_window = s + s
        left = 0
        for letter in t:
            storage[letter] += 1
        needed = 0
        
        for right in range(len(s)):
            window[s[right]] += 1
            if s[right] in storage and window[s[right]] == storage[s[right]]:
                needed += 1

            while needed == len(storage):
                if (right - left + 1) < len(min_window):
                    min_window = s[left:right + 1]
                window[s[left]] -= 1
                if s[left] in storage and window[s[left]] < storage[s[left]]:
                    needed -= 1
                left += 1
        return "" if min_window == s+s else min_window