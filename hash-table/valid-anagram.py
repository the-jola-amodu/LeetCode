class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word = {}
        drow = {}
        for letter in s:
            if letter in word:
                word[letter] += 1
            else:
                word[letter] = 1
        for letter in t:
            if letter in drow:
                drow[letter] += 1
            else:
                drow[letter] = 1
        if drow == word:
            return True
        return False

        