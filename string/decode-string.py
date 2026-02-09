class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                string = ''
                while stack[-1] != '[':
                    string = stack.pop() + string
                stack.pop()
                multiplier = ''
                while stack and stack[-1].isdigit():
                    multiplier = stack.pop() + multiplier
                stack.append(string * int(multiplier))
        return ''.join(stack)

        