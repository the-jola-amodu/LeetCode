class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for letter in s:
            if stack and letter == stack[-1][0]:
                current_letter, count = stack.pop()
                count += 1
                if count == k:
                    pass
                else:
                    stack.append((letter, count))
            else:
                stack.append((letter, 1))
        result = ''
        for tup in stack:
            result += tup[0] * tup[1]
        return result