from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        dict_bank = defaultdict(list)

        for word in strs:
            dict_bank["".join(sorted(word))].append(word)
        return dict_bank.values()