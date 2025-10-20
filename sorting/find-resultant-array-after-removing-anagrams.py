class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        to_pop = []
        for i in range(1, len(words)):
            if sorted(words[i]) == sorted(words[i - 1]):
                to_pop.append(i)
        to_pop = sorted(to_pop, reverse=True)
        for index in to_pop:
            words.pop(index)
        return words
        