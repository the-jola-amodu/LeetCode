class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combination = []

        def recurse(string, left, right):
            if left == n and right == n:
                combination.append(string)

            if left > n or right > n:
                return

            if left > right:
                recurse(string + ')', left, right + 1)
                recurse(string + '(', left + 1, right)
            elif left == right:
                recurse(string + '(', left + 1, right)
            else:
                return
        recurse('', 0, 0)
        return combination
        