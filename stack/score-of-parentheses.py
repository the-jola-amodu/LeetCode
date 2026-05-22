class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for character in s:
            if character == "(":
                stack.append(0)
            else:
                last = stack.pop()
                if last == 0:
                    stack[-1] += 1
                else:
                    stack[-1] += 2 * last
        return stack[-1]
        