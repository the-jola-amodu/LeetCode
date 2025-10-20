class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        store = {}
        counter = 0
        for letter in stones:
            if letter in store:
                store[letter] += 1
            else:
                store[letter] = 1
        for letter in jewels:
            if letter in store:
                counter += store[letter]
        return counter