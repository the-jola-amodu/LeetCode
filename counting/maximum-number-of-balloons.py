class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = 0
        if 'b' not in text or 'a' not in text or 'l' not in text or 'o' not in text or 'n' not in text:
            return counter
        bank = {}
        for letter in text:
            if letter not in bank:
                bank[letter] = 1
            else:
                bank[letter] += 1
        while True:
            bank['b'] -= 1
            bank['a'] -= 1
            bank['l'] -= 2
            bank['o'] -= 2
            bank['n'] -= 1
            if bank['b'] < 0 or bank['a'] < 0 or bank['l'] < 0 or bank['o'] < 0 or bank['n'] < 0:
                return counter
            else:
                counter += 1
        