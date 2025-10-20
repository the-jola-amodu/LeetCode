class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        dicti ={'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in range(len(s)):
            if i == 0:
                result += dicti[s[i]]
            elif dicti[s[i]] > dicti[s[i - 1]]:
                if s[i] == 'X' and s[i - 1] == 'I':
                    result += 8
                if s[i] == 'V' and s[i - 1] == 'I':
                    result += 3
                if s[i] == 'L' and s[i - 1] == 'X':
                    result += 30
                if s[i] == 'C' and s[i - 1] == 'X':
                    result += 80
                if s[i] == 'D' and s[i - 1] == 'C':
                    result += 300
                if s[i] == 'M' and s[i - 1] == 'C':
                    result += 800
            else:
                result += dicti[s[i]]
        return result