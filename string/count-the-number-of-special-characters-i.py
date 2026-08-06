class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        database = dict()
        counter = 0
        for letter in word:
            if letter.lower() not in database:
                database[letter.lower()] = set()
            if letter.islower():
                database[letter.lower()].add(1)
            else:
                database[letter.lower()].add(2)
        for letter in database:
            if database[letter] == {1, 2}:
                counter += 1
        print(database)
        return counter

        