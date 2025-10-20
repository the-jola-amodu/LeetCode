class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        word_bank = {}
        for letter in magazine:
            if letter in word_bank:
                word_bank[letter] += 1
            else:
                word_bank[letter] = 1
        for letter in ransomNote:
            if letter in word_bank:
                word_bank[letter] -= 1
                if word_bank[letter] == 0:
                    word_bank.pop(letter)
            else:
                return False
        return True
        