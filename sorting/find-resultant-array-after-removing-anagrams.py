class Solution(object):
    def removeAnagrams(self, words):
        result = [words[0]]
        for i in range(1, len(words)):
            if ''.join(sorted(words[i])) != ''.join(sorted(words[i - 1])):
                result.append(words[i])
        return result
        