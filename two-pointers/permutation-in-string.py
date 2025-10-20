from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        left = 0
        count_s1 = defaultdict(int)
        count_s2 = defaultdict(int)
        for _ in range(len(s1)):
            count_s1[s1[_]] += 1
            count_s2[s2[_]] += 1
        if count_s1 == count_s2:
            return True
        for right in range(len(s1), len(s2)):
            count_s2[s2[right]] += 1
            count_s2[s2[left]] -= 1
            if count_s2[s2[left]] == 0:
                count_s2.pop(s2[left])
            left += 1
            if count_s1 == count_s2:
                return True
        return False

        