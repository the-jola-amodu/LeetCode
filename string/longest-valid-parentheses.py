class Solution:
    def longestValidParentheses(self, s: str) -> int:
        lvp = left = right = 0

        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if right > left:
                left = right = 0
            elif left == right:
                lvp = max(lvp, left + right)
            
        left = right = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left > right:
                left = right = 0
            elif right == left:
                lvp = max(lvp, left + right)
        
        return lvp
