class Trie:

    def __init__(self):
        self.trie = dict()

    def insert(self, word: str) -> None:
        d = self.trie
        for letter in word:
            if letter not in d:
                d[letter] = dict()
            d = d[letter]
        d['.'] = '.'

    def search(self, word: str) -> bool:
        d = self.trie
        for letter in word:
            if letter not in d:
                return False
            d = d[letter]
        return '.' in d
        

    def startsWith(self, prefix: str) -> bool:
        d = self.trie
        for letter in prefix:
            if letter not in d:
                return False
            d = d[letter]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)