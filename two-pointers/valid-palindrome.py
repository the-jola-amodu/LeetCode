class Solution(object):
    def isPalindrome(self, s):
        cleaned = ""
        for i in range(len(s)):
            if s[i].lower() in "abcdefghijklmnopqrstuvwxyz1234567890":
                cleaned = s[i].lower() + cleaned
        left = 0
        right = len(cleaned) - 1

        reverse = cleaned[::-1]
        if cleaned == reverse:
            return True
        return False

        