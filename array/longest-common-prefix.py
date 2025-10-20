class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for i in range(len(min(strs, key=len))):
            common = True
            letter = strs[0][i]
            for j in range(len(strs)):
                if strs[j][i] != letter:
                    common = False
                    return prefix
            if common == True:
                prefix += letter
        return prefix
        