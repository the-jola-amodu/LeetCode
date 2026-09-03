class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def recurse(i, j):
            if i >= len(s) and j >= len(p):
                return True

            if j >= len(p):
                return False

            if (i < len(s)) and (s[i] == p[j] or p[j] == '?'):
                return recurse(i + 1, j + 1)
            if (i < len(s)) and p[j] == '*':
                return recurse(i + 1, j)
            if (i >= len(s)) and p[j] == '*':
                return True
            return False

        return recurse(0, 0)


        