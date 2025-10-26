class Solution(object):
    def findArray(self, pref):
        result = [pref[0]]
        if len(pref) == 1:
            return result
        for i in range(1, len(pref)):
            result.append(pref[i] ^ pref[i - 1])
        return result
        